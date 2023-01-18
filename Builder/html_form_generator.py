def generate_webform(text_field_list=[], checkbox_field_list=[]):
    """

    :param field_list:
    :return:

    Generate Fields
    """
    generated_fields = "\n".join(
        map(
            lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
            text_field_list
        )
    )

    generated_fields += "\n".join(
        map(
            lambda x: '<label><br><input type="checkbox" id="{0}" value="{0}">{0} <br> '.format(x),
            checkbox_field_list
        )
    )

    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html_form(text_field_list=[], checkbox_field_list=[]):
    """

    :param fields:
    :return:

    Take Field Forms and Create a WebPage using HTML and dave it in File "form_file.html"
    """
    with open("form_file.html", "w") as f:
        f.write(
            "<html><body>{}</body></html>".format(
                generate_webform(
                    text_field_list=text_field_list,
                    checkbox_field_list=checkbox_field_list
                )
            )
        )


if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    print(build_html_form(fields, checkbox_fields))
    print("HTML Generated")
