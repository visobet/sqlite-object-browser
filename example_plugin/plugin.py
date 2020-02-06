class Plugin():
    def format_title(self, title, table_name, row, is_toplevel):
        title_fields = {
            "employees": ("Employee {} {}", ("FirstName", "LastName")),
            "albums": ("Album {}", ("Title",)),
            "artists": ("Artist {}", ("Name",))
        }
        if table_name in title_fields:
            template_string, row_keys = title_fields[table_name]
            return template_string.format(*[getattr(row, key) for key in row_keys])
        elif table_name == title:
            return "Entity from table {}".format(table_name)
        else:
            return "{}: entity from table {}".format(title, table_name)

    def add_content(self, table_name, row, is_toplevel):
        return '<b><font color="red">Your add could be here!!!</font></b>'
