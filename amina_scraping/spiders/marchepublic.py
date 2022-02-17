
import scrapy
import unicodedata


class MarchepublicSpider(scrapy.Spider):
    name = 'marchepublic'
    allowed_domains = ['www.marchespublics.gov.ma']

    def __init__(self):
        self.data = {}
        self.nombre_lot = ""

    def start_requests(self):
        # urls = [
        #     "https://www.marchespublics.gov.ma/index.php?page=entreprise.EntrepriseDetailsConsultation&refConsultation=621307&orgAcronyme=d4q",
        #     "https://www.marchespublics.gov.ma/index.php?page=entreprise.EntrepriseDetailsConsultation&refConsultation=621111&orgAcronyme=o8p"
        # ]
        urls = self.url()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.data = {
            'reference':  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_reference::text').extract_first(),

            'objet_a': unicodedata.normalize('NFKC', response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_objet::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_objet::text').extract_first() == None else '-',

            'date_remise_plis_ao': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateHeureLimiteRemisePlis::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateHeureLimiteRemisePlis::text').extract_first() == None else '-',

            'acheteur_public': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_entiteAchat::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_entiteAchat::text').extract_first() == None else '-',

            'type_procedure': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_typeProcedure::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_typeProcedure::text').extract_first() == None else '-' ,

            'mode_passation': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_modePassation::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_modePassation::text').extract_first() == None else '-',

            'categorie': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_categoriePrincipale::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_categoriePrincipale::text').extract_first() == None else '-',

            'lieu_execution': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_lieuxExecutions::text').extract_first()).encode('ascii', 'ignore').decode('utf8')  if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_lieuxExecutions::text').extract_first() == None else '-',

            'estimation_ttc': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_idReferentielZoneText_RepeaterReferentielZoneText_ctl0_labelReferentielZoneText::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_idReferentielZoneText_RepeaterReferentielZoneText_ctl0_labelReferentielZoneText::text').extract_first() == None else '-',

            'reserve_pme_autoentrepreuneur_cooperative': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_idRefRadio_RepeaterReferentielRadio_ctl0_labelReferentielRadio::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_idRefRadio_RepeaterReferentielRadio_ctl0_labelReferentielRadio::text').extract_first() == None else '-',

            'lieu_retrait': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_adresseRetraitDossiers::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_adresseRetraitDossiers::text').extract_first() == None else '-',

            'lieu_depot': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_adresseDepotOffres::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_adresseDepotOffres::text').extract_first() == None else '-',

            'lieu_ouverture': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_lieuOuverturePlis::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_lieuOuverturePlis::text').extract_first() == None else '-',

            'allotissement': [],

            'echantillons': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateEchantillons::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateEchantillons::text').extract_first() == None else '-',

            'caution_provisoire': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_cautionProvisoire::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_cautionProvisoire::text').extract_first() == None else '-',

            'reunion': unicodedata.normalize('NFKC',   response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateReunion::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateReunion::text').extract_first() == None else '-',

            'variante': unicodedata.normalize('NFKC',   response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_varianteValeur::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_varianteValeur::text').extract_first() == None else '-',

            'prix_acquisition_plans': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_prixAcquisitionPlan::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_prixAcquisitionPlan::text').extract_first() == None else '-',

        }
        link = response.css(
            'a#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_linkDetailLots::attr(href)').get()

        if link:
            self.nombre_lot = response.css(
                'span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_nbrLots::text').extract_first()

            link = 'https://www.marchespublics.gov.ma/' + \
                link.replace("javascript:popUp('", '').replace("','yes')", "")
            yield response.follow(link, callback=self.fetch)
        else:
            yield self.data

    def url(self):
        with open('/home/redone/Desktop/IDA TECH/amina_scraping/procurment_links_file.txt', 'r') as f:
            return f.readlines()

    def fetch(self, response):

        while self.nombre_lot == None:
            print("**********************************************\n")
            print("NO DATA FOUND")

        print("**********************************************\n", self.nombre_lot)
        number = list(self.nombre_lot.split(" "))
        self.nombre_lot = int(number[0])
        j = 0
        for i in range(self.nombre_lot):
            key = "Lot_"+str(i+1)
            self.data['allotissement'].append(
                {
                    key: {
                        "intitule_lot": unicodedata.normalize('NFKC',  response.xpath('//div[contains(@class,"content-bloc") and contains(@class,bloc-600)]['+str(j+1) + ']/text()').get()).encode('ascii', 'ignore').decode('utf8') if not  response.xpath('//div[contains(@class,"content-bloc") and contains(@class,bloc-600)]['+str(j+1) + ']/text()').get() == None else '-',
                        "categorie_lot": unicodedata.normalize('NFKC',  response.xpath('//div[contains(@class,"content-bloc") and contains(@class,bloc-600)]['+str(j+2) + ']/text()').get()).encode('ascii', 'ignore').decode('utf8') if not   response.xpath('//div[contains(@class,"content-bloc") and contains(@class,bloc-600)]['+str(j+2) + ']/text()').get() == None else '-',
                        'description': unicodedata.normalize('NFKC',  response.xpath('//div[contains(@class,"content-bloc") and contains(@class,bloc-600)]['+str(j+3) + ']/text()').get()).encode('ascii', 'ignore').decode('utf8') if not response.xpath('//div[contains(@class,"content-bloc") and contains(@class,bloc-600)]['+str(j+3) + ']/text()').get() == None else '-',
                        "estimation_lot":  unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_idReferentielZoneTextLot_RepeaterReferentielZoneText_ctl0_labelReferentielZoneText::text').extract_first()).encode('ascii', 'ignore').decode('utf8'),
                        "caution_provisoire_lot": unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_cautionProvisoire::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_cautionProvisoire::text').extract_first() == '-' else '-',
                        "qualifications": {
                            "Qualification":  unicodedata.normalize('NFKC', list(response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_qualification > ul >li::text').extract_first().split("/"))[1]).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_qualification::text').extract_first() == '-' else '-',
                            "Sous_Qualification": unicodedata.normalize('NFKC',  list(response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_qualification  > ul >li::text').extract_first().split("/"))[2]).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_qualification::text').extract_first() == '-' else '-',
                            "Classe": unicodedata.normalize('NFKC',  list(response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_qualification  > ul >li::text').extract_first().split("/"))[3]).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_qualification::text').extract_first() == '-' else '-'
                        },
                        "agrements": {
                            "Agrements": unicodedata.normalize('NFKC',  list(response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_agrements::text').extract_first().split("/"))[1]).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl0_agrements::text').extract_first() == '-' else '-',
                            "Sous_agrements": unicodedata.normalize('NFKC',  list(response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_agrements::text').extract_first().split("/"))[2]).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl0_agrements::text').extract_first() == '-' else '-',
                            "Classe": unicodedata.normalize('NFKC',  list(response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_agrements::text').extract_first().split("/"))[3]).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl0_agrements::text').extract_first() == '-' else '-'
                        },
                        'variante': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_varianteValeur::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_varianteValeur::text').extract_first() == '-' else "-",
                        'reserve_pme_autoentrepreuneur_cooperative': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_idRefRadio_RepeaterReferentielRadio_ctl0_labelReferentielRadio::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not  response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_idRefRadio_RepeaterReferentielRadio_ctl0_labelReferentielRadio::text').extract_first() == '-' else "-",
                        'echantillons': unicodedata.normalize('NFKC',  response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_dateEchantillons::text').extract_first()).encode('ascii', 'ignore').decode('utf8') if not response.css('span#ctl0_CONTENU_PAGE_repeaterLots_ctl'+str(i)+'_dateEchantillons::text').extract_first() == '-' else "-",
                        'reunion': unicodedata.normalize('NFKC',  response.css(
                            'span#'+'ctl0_CONTENU_PAGE_repeaterLots_ctl' +
                            str(i) + '_dateReunion::text'
                        ).extract_first()).encode('ascii', 'ignore').decode('utf8') if  response.css(
                            'span#'+'ctl0_CONTENU_PAGE_repeaterLots_ctl' +
                            str(i) + '_dateReunion::text'
                        ).extract_first() == '-' else "-",
                    }

                }
            )
            j += 3
        yield self.data
