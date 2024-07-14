import pdfrw

def rename_fields(input_pdf_path, output_pdf_path, field_mapping):
    # Read the original PDF
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0]['/Annots']
    
    for annotation in annotations:
        if annotation['/Subtype'] == '/Widget':
            field = annotation['/T']
            if field:
                old_name = field.to_unicode()
                if old_name in field_mapping:
                    print(old_name)
                    new_name = field_mapping[old_name]
                    annotation.update(pdfrw.PdfDict(T=pdfrw.objects.pdfstring.PdfString.encode(new_name)))
    
    # Write the updated PDF to a new file
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

# Define the input and output PDF paths
input_pdf_path = "ISF_FORM.pdf"
output_pdf_path = "ISF_FORM_RENAMED.pdf"

# Define the field mapping (old field name to new field name)
field_mapping = {
    'Name12': 'Seller Name',
    'Address12': 'Seller Address',
    'City12': 'Seller City',
    'State12': 'Seller State',
    'Country12': 'Seller Country',
    'postal code12': 'Seller Postal Code',
    'State': 'Manufacturer State',
    'City': 'Manufacturer City',
    'Address': 'Manufacturer Address',
    'Name': 'Manufacturer Name',
    'Country': 'Manufacturer Country',
    'postal code': 'Manufacturer ZipCode',
    'Name13': 'Buyer Name',
    'Address13': 'Buyer Address',
    'City13': 'Buyer City',
    'State13': 'Buyer State',
    'Country13': 'Buyer Country',
    'postal code13': 'Buyer ZipCode',
    'Name14': 'Ship To Name',
    'Address14': 'Ship To Address',
    'City14': 'Ship To City',
    'State14': 'Ship To State',
    'Country14': 'Ship To Country',
    'postal code14': 'Ship To Postal Code',
    'Name15': 'Container Stuffing Name',
    'Address15': 'Container Stuffing Address',
    'City15': 'Container Stuffing City',
    'State15': 'Container Stuffing State',
    'Country15': 'Container Stuffing Country',
    'postal code15': 'Container Stuffing Postal Code',
    'Name16': 'Consolidator Name',
    'Address16': 'Consolidator Address',
    'City16': 'Consolidator City',
    'State16': 'Consolidator State',
    'Country16': 'Consolidator Country',
    'postal code16': 'Consolidator Postal Code',
    'Name17': 'Importer of Record Name',
    'Address17': 'Importer of Record Address',
    'City17': 'Importer of Record City',
    'State17': 'Importer of Record State',
    'Country17': 'Importer of Record Country',
    'postal code17': 'Importer of Record Postal Code',
    'Name18': 'Consignee Name',
    'Address18': 'Consignee Address',
    'City18': 'Consignee City',
    'State18': 'Consignee State',
    'Country18': 'Consignee Country',
    'postal code18': 'Consignee Postal Code',
    'Text1': 'Itemdesc1',
    'Text2': 'Itemdesc2',
    'Text3': 'Itemdesc3',
    'Text4': 'Itemdesc4',
    'Text5': 'Itemdesc5',
    'Text6': 'Itemdesc6',
    'Text7': 'Itemdesc7',
    'Text8': 'Itemdesc8',
    'Text9': 'HTSnumber1',
    'Text10': 'HTSnumber2',
    'Text11': 'HTSnumber3',
    'Text12': 'HTSnumber4',
    'Text13': 'HTSnumber5',
    'Text14': 'HTSnumber6',
    'Text15': 'HTSnumber7',
    'Text16': 'HTSnumber8',
    'Text17': 'Countryoforigin1',
    'Text18': 'Countryoforigin2',
    'Text19': 'Countryoforigin3',
    'Text20': 'Countryoforigin4',
    'Text21': 'Countryoforigin5',
    'Text22': 'Countryoforigin6',
    'Text23': 'Countryoforigin7',
    'Text24': 'Countryoforigin8'
}

# Rename the fields in the PDF
rename_fields(input_pdf_path, output_pdf_path, field_mapping)

print("Field names have been successfully renamed and saved to", output_pdf_path)
