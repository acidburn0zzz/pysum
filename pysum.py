#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import string
import hashlib

class EntryExample:
    
    def fic(self, widget):
        self.filew = gtk.FileSelection("File selection")
        
        # Connect the ok_button to file_ok_sel method
        self.filew.ok_button.connect("clicked", self.file_ok_sel)
    
        # Connect the cancel_button to destroy the widget
        self.filew.cancel_button.connect("clicked",
                                         lambda w: self.filew.destroy())
        self.filew.show()
      
    def file_ok_sel(self, w):
        # print "%s" % self.filew.get_filename()
        md5 = hashlib.md5(open(self.filew.get_filename(), 'rb').read()).hexdigest()
        #print "%s" % md5
        entry_sum.set_text(md5)
        self.filew.destroy()
	
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(600, 50)
        window.set_title("Afficher la somme MD5 du fichier")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()
    
        hbox = gtk.HBox(True, 0)
        vbox.pack_start(hbox, False, False, 0)
        hbox.show()
        
        label_sum = gtk.Label()
        global entry_sum 
        entry_sum = gtk.Entry()

        button = gtk.Button("Sélectionner un fichier")
        button.connect("clicked", self.fic)
        hbox.pack_start(button, False, False, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
 
	label_sum.set_text("Somme calculée :")
        hbox.pack_start(label_sum, False, False, 0)
        label_sum.show()

        hbox.pack_start(entry_sum, False, False, 0)
        entry_sum.set_width_chars(36)
        entry_sum.show()

        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    EntryExample()
    main()
