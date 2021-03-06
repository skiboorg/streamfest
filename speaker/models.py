from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string
import uuid
import pyqrcode
from streamfest.settings import BASE_DIR
from django.db.models.signals import post_save, post_delete



class Speaker(models.Model):
    orderPP = models.IntegerField('Номер ПП', default=10)
    name = models.CharField('ФИО', max_length=255, blank=False, null=True)
    nickName = models.CharField('Ник', max_length=255, blank=False, null=True, db_index=True)
    photo = models.ImageField('Фото)', upload_to='speaker_img/',
                              blank=False, null=True)
    pageHeader = models.ImageField('Изображение для шапки страницы', upload_to='speaker_img/', blank=False,
                                    null=True)

    nickNameSlug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    linkVK = models.CharField('Ссылка на VK', max_length=255, blank=True, null=True )
    linkTW = models.CharField('Ссылка на Twitch', max_length=255, blank=True, null=True )
    linkYT = models.CharField('Ссылка на YouTube', max_length=255, blank=True, null=True )
    linkIN = models.CharField('Ссылка на Instagram', max_length=255, blank=True, null=True)
    views = models.IntegerField('Просмотров профиля', default=0)
    about = RichTextUploadingField('Описание', blank=True, null=True)
    streaming = RichTextUploadingField('Что стримит', blank=True, null=True)
    isAtHome = models.BooleanField('Отображать на главной?', default=False)
    uniqUrl = models.CharField('Хеш для ссылки (/star/stats/)', max_length=100,  blank=True,null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.nickName)

        if not self.nickNameSlug:
            testSlug = Speaker.objects.filter(nickNameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nickNameSlug = slug + slugRandom
        if not self.uniqUrl:
            self.uniqUrl = self.nickNameSlug + '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=10))

        super(Speaker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/speaker/{}/'.format(self.nickNameSlug)

    def __str__(self):
        return 'Стример : {}'.format(self.name)

    class Meta:
        verbose_name = "Стример"
        verbose_name_plural = "Стримеры"


class Ticket(models.Model):
    streamer = models.ForeignKey(Speaker,blank=True,null=True,on_delete=models.CASCADE,verbose_name='Билет от стримера',
                             related_name='user_item', db_index=True)
    article = models.CharField('Артикул', max_length=100, blank=True, null=True, db_index=True)

    isDefaultOneDayTicket = models.BooleanField('Это билет на 1 день?', default=False, db_index=True)
    isDefaultTwoDayTicket = models.BooleanField('Это билет на 2 дня?', default=False, db_index=True)
    price = models.IntegerField('Цена билета. Эта цена будет применена ко всем билетам', default=0)
    sells = models.IntegerField('Всего продаж', default=0)


    def __str__(self):
        if self.streamer:
            ticketType = self.article.split('_')[1]
            print(ticketType)
            isOneday = None
            isTwoday = None
            try:
                isOneday=Ticket.objects.get(article=ticketType, isDefaultOneDayTicket=True)
            except:
                isOneday = None
            try:
                isTwoday = Ticket.objects.get(article=ticketType, isDefaultTwoDayTicket=True)
            except:
                isTwoday = None
            print('isOneday=',isOneday)
            print('isTwoday=',isTwoday)
            if isOneday:
                return 'Билет от стримера : {} на один день'.format(self.streamer.name)
            if isTwoday:
                return 'Билет от стримера : {} на два дня'.format(self.streamer.name)
        else:
            if self.isDefaultOneDayTicket:
                return 'Обычный билет на 1 день'
            if self.isDefaultTwoDayTicket:
                return 'Обычный билет на 2 дня'
    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"


class Order(models.Model):
    streamer = models.ForeignKey(Speaker,blank=True,null=True, on_delete=models.CASCADE,
                                     verbose_name='Билет от')
    customerFio = models.CharField("ФИО покупателя", max_length=255, blank=False, null=True)
    customerPhone = models.CharField("Телефон покупателя", max_length=255, blank=False, null=True)
    customerEmail = models.CharField("E-Mail покупателя", max_length=255, blank=False, null=True)
    ticket = models.ForeignKey(Ticket, blank=True,null=True, on_delete=models.CASCADE,
                                     verbose_name='Заказан')
    price = models.IntegerField('Сумма', default=0)
    isCheckIn = models.BooleanField('Погашен', default=False)
    isSpecial = models.BooleanField('Специальный заказ', default=False)
    codeQR = models.CharField('Случайное число для QR кода', max_length=255, blank=True, null=True, editable=False)
    imageQR = models.CharField('QR код', max_length=255, blank=True, null=True, editable=False)
    isPayed = models.BooleanField('Оплачено', default=False)
    createdAt = models.DateTimeField('Заказ создан', auto_now_add=True)
    updatedAt = models.DateTimeField('Заказ изменен', auto_now=True)

    def __str__(self):
        if self.isPayed:
            return f'Оплаченный заказ №-{self.id} от {self.customerFio}'
        else:
            return f'Не оплаченный заказ №-{self.id} от {self.customerFio}'
    #str(uuid.uuid4()) img = qrcode.make('Some data here')

    # def save(self, *args, **kwargs):
    #     print(BASE_DIR)
    #     super(Order, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

def createSpeakerItem(sender, instance, created, **kwargs):
    if created:
        oneDayArticle = Ticket.objects.get(isDefaultOneDayTicket=True)
        twoDayArticle = Ticket.objects.get(isDefaultTwoDayTicket=True)
        Ticket.objects.create(streamer=instance,
                              article=f'{instance.nickNameSlug}_{oneDayArticle.article}')
        Ticket.objects.create(streamer=instance,
                              article=f'{instance.nickNameSlug}_{twoDayArticle.article}')

def createOrder(sender, instance, created, **kwargs):
    if created:
        print('Create QR')
        codeQR = str(uuid.uuid4())
        instance.codeQR = codeQR
        url = pyqrcode.create(f'https://streamfest.ru/check_order/{codeQR}')
        url.png(f'{BASE_DIR}\media\qrcodes\{instance.id}.png', scale=10)
        instance.imageQR = f'\media\qrcodes\{instance.id}.png'
        instance.save()
post_save.connect(createOrder, sender=Order)
post_save.connect(createSpeakerItem, sender=Speaker)