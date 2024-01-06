class TypeSysLicenceStatus:
    TYPE_AT = "AT"
    TYPE_PA = "PA"
    TYPE_PF = "PF"
    TYPE_IN = "IN"


    array = (TYPE_AT,
            TYPE_PA,
            TYPE_PF,
            TYPE_IN)
    
    choices = (
        (TYPE_AT,"Ativo"), 
        (TYPE_PA,"Pend. Ativação"),
        (TYPE_PF,"Pend. Financeira"), 
        (TYPE_IN,"Inativa")
    )
#==========================================================
class TypeSysPlan:
        TYPE_FR = "FR"
        TYPE_TR = "TR"
        TYPE_PG = "PG"
        

        array = (TYPE_FR,
                TYPE_TR,
                TYPE_PG)
        
        choices = (
            (TYPE_FR,"FREE"), 
            (TYPE_TR,"Pend. Trial"),
            (TYPE_PG,"Pend. Pago")
            
    )
#==========================================================
class TypeSysprogram:
        TYPE_T = "T"
        TYPE_L = "L"
        TYPE_P = "P"
        TYPE_U = "U"
        

        array = (TYPE_T,
                 TYPE_L,
                 TYPE_P,
                 TYPE_U
                 )
        
        choices = (
            (TYPE_T,"Tabelas"), 
            (TYPE_L,"Lançamento"),
            (TYPE_P,"Processamento"),
            (TYPE_U,"Utilitário")
            
    )
#==========================================================
class TypeSysUserOrigem:   
        TYPE_1 = 1
        TYPE_2 = 2
        array = (TYPE_1,
                 TYPE_2
                 )
        
        choices = (
            (TYPE_1,"Local"), 
            (TYPE_2,"Chat"), 
            
    )

#==========================================================
class TypeSysDocumentContentType:   
        TYPE_PDF = "application/pdf"
        TYPE_TXT = "application/txt"
        TYPE_ZIP = "application/zip"
        TYPE_OTS = "application/octet-stream"

        TYPE_GIF = "application/gif"
        TYPE_PNG = "application/png"
        TYPE_JPEG = "application/jpeg"
        TYPE_BMP = "application/bmp"
        TYPE_WEBP = "application/webp"

        TYPE_PLAIN = "application/plain"
        TYPE_HTML= "application/html"
        TYPE_CSS = "application/css"

        TYPE_PKCS12 = "application/pkcs12"
        TYPE_VDN_MSPOWERPOINT = "application/vnd.mspowerpoint"
        TYPE_XLSX = "application/xlsx"
        TYPE_XML = "application/xml"
        

        array = (TYPE_PDF,
                 TYPE_TXT,
                 TYPE_ZIP,
                 TYPE_OTS,

                 TYPE_GIF,
                 TYPE_PNG,
                 TYPE_JPEG,
                 TYPE_BMP,
                 TYPE_WEBP,

                 TYPE_PLAIN,
                 TYPE_HTML,
                 TYPE_CSS,

                 TYPE_PKCS12,
                 TYPE_VDN_MSPOWERPOINT,
                 TYPE_XLSX,
                 TYPE_XML
                
                 )
        
        choices = (
            (TYPE_PDF,"Pdf"), 
            (TYPE_TXT,"Texto"),
            (TYPE_ZIP,"Zip"), 
            (TYPE_OTS,"Ots"), 
            (TYPE_GIF,"Gif"), 
            (TYPE_PNG,"Png"), 
            (TYPE_JPEG,"Jpeg"), 
            (TYPE_BMP,"Bmp"), 
            (TYPE_WEBP,"Webp"), 
            (TYPE_PLAIN,"Plain"),
            (TYPE_HTML,"Html"), 
            (TYPE_CSS,"Css"), 
            (TYPE_PKCS12,"Pkcs12"), 
            (TYPE_VDN_MSPOWERPOINT,"Vdn_mspowerpoint"), 
            (TYPE_XLSX,"xlsx"), 
            (TYPE_XML,"Xml"), 
            
            
    )    



    




