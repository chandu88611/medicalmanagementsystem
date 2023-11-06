from django.db import models

class Billing(models.Model):
    # Common fields for both invoices and receipts
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # You need to define the Customer model
    # Additional fields for invoices
    is_invoice = models.BooleanField(default=True)
    invoice_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    # Additional fields for receipts
    is_receipt = models.BooleanField(default=False)
    receipt_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.is_invoice and not self.invoice_number:
            # Generate an invoice number (e.g., INV-0001)
            last_invoice = Billing.objects.filter(is_invoice=True).order_by('-invoice_number').first()
            if last_invoice:
                last_number = int(last_invoice.invoice_number.split('-')[1])
                self.invoice_number = f'INV-{str(last_number + 1).zfill(4)}'
            else:
                self.invoice_number = 'INV-0001'

        if self.is_receipt and not self.receipt_number:
            # Generate a receipt number (e.g., RECEIPT-0001)
            last_receipt = Billing.objects.filter(is_receipt=True).order_by('-receipt_number').first()
            if last_receipt:
                last_number = int(last_receipt.receipt_number.split('-')[1])
                self.receipt_number = f'RECEIPT-{str(last_number + 1).zfill(4)}'
            else:
                self.receipt_number = 'RECEIPT-0001'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number if self.is_invoice else self.receipt_number
