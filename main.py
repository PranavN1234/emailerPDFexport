import PyPDF2
from ai_parser import extract_bol_data
from field_mapping import field_mapping

parsed_data = extract_bol_data("data.txt")
field_mapping = field_mapping

# Function to fill the PDF with data
def fill_pdf(input_pdf_path, output_pdf_path, data, field_mapping):
    with open(input_pdf_path, "rb") as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

            # Fill the fields with data
            for key, value in data.items():
                if key in field_mapping:
                    field_name = field_mapping[key]
                    if value is not None:
                        pdf_writer.update_page_form_field_values(pdf_writer.pages[page_num], {field_name: value})

            # Handle items separately
            if "items" in data:
                items = data["items"]
                for i, item in enumerate(items, start=1):
                    item_desc_key = f"Itemdesc{i}"
                    hts_number_key = f"HTSnumber{i}"
                    country_origin_key = f"Countryoforigin{i}"

                    item_desc_value = item.get("description", "")
                    hts_number_value = item.get("hts_number", "")
                    country_origin_value = item.get("country_of_origin", "")

                    pdf_writer.update_page_form_field_values(pdf_writer.pages[page_num], {
                        item_desc_key: item_desc_value,
                        hts_number_key: hts_number_value,
                        country_origin_key: country_origin_value
                    })

        # Write the filled PDF to a new file
        with open(output_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)

# Define the input and output PDF paths
input_pdf_path = "ISF_FORM_RENAMED.pdf"
output_pdf_path = "ISF_FORM_FILLED.pdf"

# Fill the PDF with placeholder values and print the fields
fill_pdf(input_pdf_path, output_pdf_path, parsed_data, field_mapping)
