# Invoice Number Generator
# Finance wants invoice numbers like INV-DEL-2026-00042

invoice = "INV-DEL-2026-00042".split("-")

branch = invoice[0]
branch_code = invoice[1]
year = invoice[2]


invoice_number = input("Enter a number : ")

if int(invoice_number) > 0:
    if int(invoice_number) > 99999:
        print(f"Invoice number overflow")

    else:
        number_generate = invoice_number.zfill(5)
        new_invoice = branch +"-"+ branch_code +"-"+ year +"-"+ str(number_generate)
        print(f"Invoice : {new_invoice}")
else:
    print(f"Value must be positive")
                

