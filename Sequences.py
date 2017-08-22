import logging
from json import dumps
class Sequences:
    def __init__(self, name):
        """

        :param name:
        """
        self.logger = logging.getLogger("sequence")
        self.name = name

    def send_to(self, to, msg=""):
        return self.seq_tool(msg, to, )

    def reply_to(self, to, msg=""):
        return self.seq_tool(msg, to, dotted=True)

    def task(self, content):

        return self.seq_tool(msg=content, box=False, to=self.name)

    def reply_from(self, origin="Origin_Name", msg=""):
        return self.seq_tool(msg=msg, to=self.name, dotted=True, alt_name=origin)

    def message_from(self, origin="Origin_Name", msg=""):
        return self.seq_tool(msg=msg, to=self.name, dotted=False, alt_name=origin)

    def activate(self):
        return self.seq_form("activate " + self.name)

    def deactivate(self):
        return self.seq_form("deactivate " + self.name)

    def seq_tool(self, msg=None, to="Change_Me", box=False, dotted=False, alt_name=False):
        name = self.name
        if alt_name:
            name = alt_name
        if box:
            form = 'Note over {}: {}'.format(name, msg)
            return self.seq_form(form, )
        elif dotted:
            form = "{}-->{}: {}".format(name, to, msg)
            return self.seq_form(form)
        else:
            form = "{}->{}: {}".format(name, to, msg)
            return self.seq_form(form)

    def opt(self, op_name="", end=False):
        if end:
            return self.seq_form("end")
        return self.seq_form("opt "+op_name)

    def seq_form(self, line):
        self.logger.info(dumps({"seq": line, "time": time.time()}))
        return {"seq": {}}
