import os
import subprocess

class Linguakit:
    
    LANGUAGE_SCRIPT = "perl"
    PATH_SCRIPT_ANALYZE = "C:\\Users\\Aurinez\\Desktop\\Linguakit\\linguakit.perl"

    def __init__ (self, language_text = 'pt', output_mode = '-s', off_shell = True):
        self._language_text = language_text
        self._output_mode = output_mode
        self._off_shell = off_shell

    def sent_analyze(self, text):
        result = subprocess.check_output([self.LANGUAGE_SCRIPT,self.PATH_SCRIPT_ANALYZE, 'sent',
         self._language_text, text, self._output_mode], shell = self._off_shell)
        rList =  result.decode().replace('\r','\t').split('\t')
        sent = rList[1]
        sent_value = rList[2]
        return [sent_value]



