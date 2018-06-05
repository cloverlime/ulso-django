from django.db import models
from django.utils import timezone


class Account(models.Model):
    """"Student Central gives its societies three separate pots of grant money.
        All three pots must be used up by the end of the year."""
    ACCOUNT_TYPE = (
    ("Matched", "Matched"),
    ("Equipment","Equipment"),
    ("Facilities","Facilities"),
    ("Self-Raised Funds", "Self-Raised Funds"),
    ("Cashbox" ,"Cashbox"),
    )

    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE, help_text='Student Central grants reset every year.')
    academic_year = models.CharField(max_length=10, help_text="e.g. 2018/19")

    name = models.CharField(max_length=20,
                            blank=True,
                            null=True,
                            help_text='You can choose to give the account a different name from the default')

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    start_balance = models.DecimalField(max_digits=10,
                               decimal_places=2,
                               blank=True,
                               null=True,
                               help_text="How much did we get from SC at \
                               the start of the academic year?")

    notes = models.CharField(max_length=300,
                             blank=True,
                             null=True,
                             help_text="e.g. describe the uses \
                             for this account")


    def __str__(self):
        if not self.name:
            return '{} {}'.format(self.account_type, self.academic_year)
        return '{} {}'.format(self.name, self.academic_year)


    def save(self, *args, **kwargs):
        if not self.id and self.start_balance > 0:
            self.balance = self.start_balance
        # self.start_balance = Account.calculate_balance()
        return super(Account, self).save(*args, **kwargs)


class Transaction(models.Model):

    date = models.DateTimeField(editable=False, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    deposit = models.DecimalField("In £", max_digits=10, decimal_places=2, default=0, help_text="Enter positive number")
    withdraw = models.DecimalField("Out £", max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=50, help_text="What was this transaction for?")
    paid_to_or_from = models.CharField("Paid to/Received from", max_length=30, blank=True, null=True, help_text="Leave blank if money was received")
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.description

    def calculate_balance(self):
        self.account.balance = self.account.balance - self.withdraw + self.deposit
        return self.account.save()

    def save(self, *args, **kwargs):
        # Create the date upon saving for the first time.
        if not self.id or not self.date:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(Transaction, self).save(*args, **kwargs)
        return self.calculate_balance()

    # TODO Fix this... it's currently not working :(
    def delete(self, *args, **kwargs):
        self.account.balance = self.account.balance + self.withdraw - self.deposit
        return super(Transaction, self).delete(*args, **kwargs)
