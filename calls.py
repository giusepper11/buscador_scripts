# -*- coding: utf-8 -*-

import sys
from bib_to_xml import BibtoXML
from slor_load_xml import Solr_load_xml


collection = {
    'wos': ['/var/tmp/bibtex/', '.xml', 'xml_out/', '192.168.0.212:8983', 'wos', 'text/xml'],

}

def executa(coll):
    """
    :param coll: argumento para selecionar collection que será executada ex. "python calls.py wos" para webOfScience

    """

    if coll == 'wos':
        param = collection['wos']
        bibxml = BibtoXML(param[0])
        bibxml.parse_bib()  # gera XML
        # #######################################
        slorload = Solr_load_xml(param[2], param[1], param[3], param[4], param[5])
        slorload.files_load()  # carrega no server
    else:
        print('digite collection como parametro')


if __name__ == "__main__":
    try:
        executa(sys.argv[1])
    except IndexError:
        print('digite collection como parametro')
