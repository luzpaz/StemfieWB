import StemfieWb_locator
import os
global StemfieWBpath
global StemfieWB_icons_path
StemfieWBpath = os.path.dirname(StemfieWb_locator.__file__)
StemfieWB_icons_path = os.path.join( StemfieWBpath, 'Icons')

#global main_StemfieWB_Icon
#main_StemfieWB_Icon = os.path.join( StemfieWB_icons_path , 'Stemfie_-_Logo_48x48.png')

class StemfieWorkbench (Workbench): 
    MenuText = "STEMFIE"
    ToolTip = "Banco trabajo para Stemfie"
    Icon = ( StemfieWB_icons_path + "/Stemfie_-_Logo_48x48.png")

    def Initialize(self):
        import Stemfie                                  # Carga el modulo 'Stemfie.py'

        #  Lista Brazos
        self.ListaBrazos = [
            "STEMFIE_Brace_STR_STD_ERR",
            "STEMFIE_Brace_STR_STD_BRD_AZ",
            "STEMFIE_Brace_CRN_ERR_ASYM",
            "STEMFIE_Brace_STR_STD_BRM",
            "STEMFIE_Brace_STR_STD_BRM_AY",
            "STEMFIE_Brace_STR_SLT_BE_SYM_ERR",
            "STEMFIE_Brace_STR_SLT_CNT_ERR",
            "STEMFIE_Brace_STR_SLT_FL_ERR",
            "STEMFIE_Brace_STR_SLT_SE_ERR",
            "STEMFIE_Brace_STR_STD_BRD_AY",
            "STEMFIE_Brace_STR_STD_BRT_AZ",
            "STEMFIE_Brace_STR_STD_BRT_AY",
            "STEMFIE_Brace_STR_STD_CR",
        ]
        self.appendToolbar(
            "Stemfie Brace", self.ListaBrazos
        )  # crea una barra de herramientas 'Stemfie Brace' con los iconos de los comandos

        #   Lista Vigas
        self.ListaVigas = [
            "STEMFIE_Beam_STR_ESS",
            "STEMFIE_Beam_STR_ERR",
            "STEMFIE_Beam_STR_BEM",
            "STEMFIE_Beam_AGD_ESS_USH_SYM",
            "STEMFIE_Beam_STR_BED",
            "STEMFIE_Beam_STR_BET",
            "STEMFIE_Beam_STR_BXS_ESS_H",
            "STEMFIE_Beam_STR_BXS_ESS_C",
        ]
        self.appendToolbar(
            "Stemfie Beam", self.ListaVigas
        )  # crea una barra de herramientas 'Stemfie Beam' con los iconos de los comandos

        #   Lista Conectores
        self.ListaConectores = [
            "STEMFIE_Conector_THR_H_BEM_SFT_1W",
            "STEMFIE_Conector_THR_H_BEM_SFT_2W_180",
            "STEMFIE_Conector_THR_H_BEM_SFT_2W_90",
            "STEMFIE_Conector_THR_H_BEM_SFT_3W",
            "STEMFIE_Conector_THR_H_BEM_SFT_4W",
        ]

        #   Lista Comandos
        self.ListaComandos = ["Cmd_Listado"]
        self.appendToolbar("Comandos",self.ListaComandos)  # crea una barra de herramientas 'Stemfie Comandos' con los iconos de los comandos


        # Creamos menu 
        self.appendMenu("Stemfie",self.ListaComandos)
        # Creo submenus
        self.appendMenu(["Stemfie","Braces"],self.ListaBrazos)
        self.appendMenu(['Stemfie','Beams'],self.ListaVigas)
        self.appendMenu(['Stemfie','Connectors'],self.ListaConectores)

"""    def ContextMenu(self, recipient):
       
       self.appendContextMenu("Stemfie",self.ListaBrazos)
       
       import FreeCAD, FreeCADGui
        selection = [s  for s in FreeCADGui.Selection.getSelection() if s.Document == FreeCAD.ActiveDocument ]
        if len(selection) == 1:
            obj = selection[0]
            if 'sourceFile' in  obj.Content:
                self.appendContextMenu("Stemfie", self.ListaBrazos )

"""


Gui.addWorkbench(StemfieWorkbench())                # Carga las barras de herramientas que se denominen
