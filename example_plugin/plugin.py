class Plugin():
    title_fields = {
            "employees": ("Employee {} {}", ("FirstName", "LastName")),
            "albums": ("Album {}", ("Title",)),
            "artists": ("Artist {}", ("Name",)),
            "playlists": ("Playlist '{}'", ("Name",)),
            "tracks": ("Track: {}", ("Name",))

        }
    def format_title(self, title, table_name, row, is_toplevel):
        if table_name in self.title_fields:
            template_string, row_keys = self.title_fields[table_name]
            return template_string.format(*[
                recursive_getattr(row, key) for key in row_keys])
        else:
            return title

    def format_entry(self, title, table_name, row_dict):
        if table_name in self.title_fields:
            template_string, row_keys = self.title_fields[table_name]
            return template_string.format(*[
                recursive_getattr(row_dict, key) for key in row_keys])
        else:
            return title

    def add_content(self, table_name, row, is_toplevel):
        return ""#'<b><font color="red">Your add could be here!!!</font></b>'

def recursive_getattr(row, key):
    keys = key.split(".")
    curr_row = row
    for key in keys:
        try:
            curr_row = getattr(curr_row, key)
        except AttributeError:
            curr_row = curr_row[key]
    return curr_row