from django.db import models
from django.contrib.auth.models import User

class Sectors(models.Model):
    sname=models.CharField(max_length=60,)
    DClose=models.DecimalField(max_digits=7,decimal_places=2)
    WClose=models.DecimalField(max_digits=7,decimal_places=2)


    def __str__(self):
        return str(self.sname)+" "+str(self.DClose)+"   "+str(self.WClose)

class perform_metric(models.Model):
    sname=models.ForeignKey(Sectors,on_delete=models.CASCADE,related_name='sectors')
    sharpeRatio=models.DecimalField(max_digits=7,decimal_places=5)

    def _str_(self):
        return self.sname

class Futures(models.Model):
    symbol=models.CharField(max_length=30)
    exp_dt=models.DateField()
    Open=models.DecimalField(max_digits=7,decimal_places=2)
    high=models.DecimalField(max_digits=7,decimal_places=2)
    low=models.DecimalField(max_digits=7,decimal_places=2)
    close=models.DecimalField(max_digits=7,decimal_places=2)
    settlePrice=models.DecimalField(max_digits=7,decimal_places=2)
    Contract=models.IntegerField()
    valnInLakhs=models.IntegerField()
    openI=models.IntegerField()
    deltaOI=models.IntegerField()
    TimeS=models.DateField()

    def __str__(self):
        #return self.symbol+"  "+self.exp_dt+"   "+self.Open+"  "+self.high+"  "+self.low+"    "+self.close+"  "+self.settlePrice+"  "+self.Contract+"  "+self.openI+"   "+self.deltaOI+"   "+self.TimeS
        return str(self.symbol)+"   "+str(self.Open)+"  "+str(self.high)
    
class Future_Sectors(models.Model):
    symbol=models.ForeignKey(Futures,on_delete=models.CASCADE,related_name='future')
    sname=models.ForeignKey(Sectors,on_delete=models.CASCADE,related_name='sector')

class Options(models.Model):
    symbol=models.CharField(max_length=30)
    exp_dt=models.DateField()
    strikePrice=models.IntegerField()
    otype=models.CharField(max_length=15)
    Open=models.DecimalField(max_digits=7,decimal_places=2)
    high=models.DecimalField(max_digits=7,decimal_places=2)
    low=models.DecimalField(max_digits=7,decimal_places=2)
    close=models.DecimalField(max_digits=7,decimal_places=2)
    settlePrice=models.DecimalField(max_digits=7,decimal_places=2)
    openI=models.IntegerField()
    deltaOI=models.IntegerField()
    TimeS=models.DateField()

    def __str__(self):
        #return self.symbol+"  "+self.exp_dt+"   "+self.otype+"  "+self.Open+"  "+self.high+"  "+self.low+"    "+self.close+"  "+self.settlePrice+"  "+self.openI+"   "+self.deltaOI+"   "+self.TimeS
        return str(self.symbol)+"   "+str(self.Open)+"  "+str(self.high)

class option_Sectors(models.Model):
    symbol=models.ForeignKey(Options,on_delete=models.CASCADE,related_name='option')
    sname=models.ForeignKey(Sectors,on_delete=models.CASCADE,related_name='tosector')

class Most_Volatile_Futures(models.Model):
    symbol=models.ForeignKey(Futures,on_delete=models.CASCADE,related_name='futures')
    quality=models.CharField(max_length=15)
    change=models.IntegerField()

    def __str__(self):
        f=Futures.objects.get(pk=self.symbol_id)
        #s=self.quality+"    "+str(self.change())
        return  "        "+f.symbol+"              "+self.quality+"          "+str(self.change)

class Most_Volatile_Options(models.Model):
    symbol=models.ForeignKey(Options,on_delete=models.CASCADE,related_name='options')
    quality=models.CharField(max_length=15)
    change=models.IntegerField()

    def __str__(self):
        f=Options.objects.get(pk=self.symbol_id)
        #s=self.quality+"    "+str(self.change())
        return  "        "+f.symbol+"              "+self.quality+"          "+str(self.change)

class UserFutures(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    symbol=models.ForeignKey(Futures,on_delete=models.CASCADE,related_name='currentFutures')
    quantity=models.IntegerField()

class UserOptions(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    symbol=models.ForeignKey(Options,on_delete=models.CASCADE,related_name='currentOptions')
    quantity=models.IntegerField()

class UserRecordFutures(models.Model):
    #username=models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='Users')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    symbol=models.ForeignKey(Futures,on_delete=models.CASCADE,related_name='investedFutures')
    quantity=models.IntegerField()

class UserRecordOptions(models.Model):
    #username=models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='users')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    symbol=models.ForeignKey(Options,on_delete=models.CASCADE,related_name='investedOptions')
    quantity=models.IntegerField()

class FutureSearches(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    symbol=models.ForeignKey(Futures,on_delete=models.CASCADE,related_name='SearchFutures')
    
class OptionSearches(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    symbol=models.ForeignKey(Options,on_delete=models.CASCADE,related_name='SearchOptions')
    
