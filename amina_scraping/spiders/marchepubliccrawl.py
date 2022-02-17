import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MarchepubliccrawlSpider(CrawlSpider):
    name = 'marchepubliccrawl'
    allowed_domains = ['www.marchespublics.gov.ma']
    start_urls = [
        'https://www.marchespublics.gov.ma/index.php?page=entreprise.EntrepriseAdvancedSearch&WithCritere&searchAnnCons']


    

    le_det =LinkExtractor(restrict_xpaths='//div[contains(@class,"action")] /a[1]')
    rule_det = Rule(
        le_det,
        callback='parse_item',
        follow=False
    )
    le_pagination = LinkExtractor( restrict_css='a#ctl0_CONTENU_PAGE_resultSearch_PagerBottom_ctl2::attr(href)')
    rule_pagination = Rule(
        le_pagination,
        follow=True
    )

    # rule_pagi = Rule(
    #     LinkExtractor(allow=r'Items/'),
    #     callback='parse_item',
    #     follow=True)
    rules = (
        rule_det,rule_pagination
    )

    def parse_item(self, response):
        data = {
            'reference': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_reference::text').extract_first(),

            'objet_ao':  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_objet::text').extract_first(),

            'date_remise_plis_ao': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateHeureLimiteRemisePlis::text').extract_first(),

            'acheteur_public': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_entiteAchat::text').extract_first(),

            'type_procedure': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_typeProcedure::text').extract_first(),

            'mode_passation': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_modePassation::text').extract_first(),

            'categorie': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_categoriePrincipale::text').extract_first(),

            'lieu_execution': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_lieuxExecutions::text').extract_first(),

            'estimation_ttc': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_idReferentielZoneText_RepeaterReferentielZoneText_ctl0_labelReferentielZoneText::text').extract_first(),

            'reserve_pme_autoentrepreuneur_cooperative': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_idRefRadio_RepeaterReferentielRadio_ctl0_labelReferentielRadio::text').extract_first(),

            'lieu_retrait': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_adresseRetraitDossiers::text').extract_first(),

            'lieu_depot': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_adresseDepotOffres::text').extract_first(),

            'lieu_ouverture': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_lieuOuverturePlis::text').extract_first(),

            'allotissement': [],

            'echantillons': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateEchantillons::text').extract_first(),

            'caution_provisoire': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_cautionProvisoire::text').extract_first(),

            'reunion':  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_dateReunion::text').extract_first(),

            'variante':  response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_varianteValeur::text').extract_first(),

            'prix_acquisition_plans': response.css('span#ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_prixAcquisitionPlan::text').extract_first(),
        }
        yield data 
