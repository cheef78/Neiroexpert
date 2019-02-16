<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class MainForm
    Inherits System.Windows.Forms.Form

    'Форма переопределяет dispose для очистки списка компонентов.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Является обязательной для конструктора форм Windows Forms
    Private components As System.ComponentModel.IContainer

    'Примечание: следующая процедура является обязательной для конструктора форм Windows Forms
    'Для ее изменения используйте конструктор форм Windows Form.  
    'Не изменяйте ее в редакторе исходного кода.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Dim Exit_MainMenu As System.Windows.Forms.ToolStripMenuItem
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(MainForm))
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.File_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Openraschet_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Saveraschet_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.OpenTEObase_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.SaveTEObase_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.WayStruct_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.PlanProf_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.VSP_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Open_WayStruct_Base_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Ekspluslov_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Vagonpotok_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Climat_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Prognose_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Loadiv_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.LoadivVeip_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.LoadivNeiro_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.LoadivGist_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.TEOcriteria_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.TEOcritPrice_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.TEOcritRemont_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.TEOcritBezop_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.TEOcritDegrad_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.PlanTER_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.PrognosCalc_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.TERReport_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.Help_mainmenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.ОПрограммеToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.РазработчикиToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.Open_raschet = New System.Windows.Forms.OpenFileDialog()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Open_TEO_base = New System.Windows.Forms.OpenFileDialog()
        Me.Save_raschet = New System.Windows.Forms.SaveFileDialog()
        Me.Save_TEO_base = New System.Windows.Forms.SaveFileDialog()
        Me.Open_pl_prof_vsp_base = New System.Windows.Forms.OpenFileDialog()
        Me.Open_gist_force = New System.Windows.Forms.OpenFileDialog()
        Exit_MainMenu = New System.Windows.Forms.ToolStripMenuItem()
        Me.MenuStrip1.SuspendLayout()
        Me.SuspendLayout()
        '
        'Exit_MainMenu
        '
        Exit_MainMenu.Name = "Exit_MainMenu"
        resources.ApplyResources(Exit_MainMenu, "Exit_MainMenu")
        AddHandler Exit_MainMenu.Click, AddressOf Me.ВыходAltXToolStripMenuItem_Click
        '
        'MenuStrip1
        '
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.File_mainmenu, Me.WayStruct_mainmenu, Me.Ekspluslov_mainmenu, Me.Prognose_mainmenu, Me.Help_mainmenu})
        resources.ApplyResources(Me.MenuStrip1, "MenuStrip1")
        Me.MenuStrip1.Name = "MenuStrip1"
        '
        'File_mainmenu
        '
        Me.File_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.Openraschet_mainmenu, Me.Saveraschet_mainmenu, Me.OpenTEObase_mainmenu, Me.SaveTEObase_mainmenu, Exit_MainMenu})
        Me.File_mainmenu.Name = "File_mainmenu"
        resources.ApplyResources(Me.File_mainmenu, "File_mainmenu")
        '
        'Openraschet_mainmenu
        '
        Me.Openraschet_mainmenu.Name = "Openraschet_mainmenu"
        resources.ApplyResources(Me.Openraschet_mainmenu, "Openraschet_mainmenu")
        '
        'Saveraschet_mainmenu
        '
        Me.Saveraschet_mainmenu.Name = "Saveraschet_mainmenu"
        resources.ApplyResources(Me.Saveraschet_mainmenu, "Saveraschet_mainmenu")
        '
        'OpenTEObase_mainmenu
        '
        Me.OpenTEObase_mainmenu.Name = "OpenTEObase_mainmenu"
        resources.ApplyResources(Me.OpenTEObase_mainmenu, "OpenTEObase_mainmenu")
        '
        'SaveTEObase_mainmenu
        '
        Me.SaveTEObase_mainmenu.Name = "SaveTEObase_mainmenu"
        resources.ApplyResources(Me.SaveTEObase_mainmenu, "SaveTEObase_mainmenu")
        '
        'WayStruct_mainmenu
        '
        Me.WayStruct_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.PlanProf_mainmenu, Me.VSP_mainmenu, Me.Open_WayStruct_Base_mainmenu})
        Me.WayStruct_mainmenu.Name = "WayStruct_mainmenu"
        resources.ApplyResources(Me.WayStruct_mainmenu, "WayStruct_mainmenu")
        '
        'PlanProf_mainmenu
        '
        Me.PlanProf_mainmenu.Name = "PlanProf_mainmenu"
        resources.ApplyResources(Me.PlanProf_mainmenu, "PlanProf_mainmenu")
        '
        'VSP_mainmenu
        '
        Me.VSP_mainmenu.Name = "VSP_mainmenu"
        resources.ApplyResources(Me.VSP_mainmenu, "VSP_mainmenu")
        '
        'Open_WayStruct_Base_mainmenu
        '
        Me.Open_WayStruct_Base_mainmenu.Name = "Open_WayStruct_Base_mainmenu"
        resources.ApplyResources(Me.Open_WayStruct_Base_mainmenu, "Open_WayStruct_Base_mainmenu")
        '
        'Ekspluslov_mainmenu
        '
        Me.Ekspluslov_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.Vagonpotok_mainmenu, Me.Climat_mainmenu})
        Me.Ekspluslov_mainmenu.Name = "Ekspluslov_mainmenu"
        resources.ApplyResources(Me.Ekspluslov_mainmenu, "Ekspluslov_mainmenu")
        '
        'Vagonpotok_mainmenu
        '
        Me.Vagonpotok_mainmenu.Name = "Vagonpotok_mainmenu"
        resources.ApplyResources(Me.Vagonpotok_mainmenu, "Vagonpotok_mainmenu")
        '
        'Climat_mainmenu
        '
        Me.Climat_mainmenu.Name = "Climat_mainmenu"
        resources.ApplyResources(Me.Climat_mainmenu, "Climat_mainmenu")
        '
        'Prognose_mainmenu
        '
        Me.Prognose_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.Loadiv_mainmenu, Me.TEOcriteria_mainmenu, Me.PlanTER_mainmenu})
        Me.Prognose_mainmenu.Name = "Prognose_mainmenu"
        resources.ApplyResources(Me.Prognose_mainmenu, "Prognose_mainmenu")
        '
        'Loadiv_mainmenu
        '
        Me.Loadiv_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.LoadivVeip_mainmenu, Me.LoadivNeiro_mainmenu, Me.LoadivGist_mainmenu})
        Me.Loadiv_mainmenu.Name = "Loadiv_mainmenu"
        resources.ApplyResources(Me.Loadiv_mainmenu, "Loadiv_mainmenu")
        '
        'LoadivVeip_mainmenu
        '
        Me.LoadivVeip_mainmenu.Name = "LoadivVeip_mainmenu"
        resources.ApplyResources(Me.LoadivVeip_mainmenu, "LoadivVeip_mainmenu")
        '
        'LoadivNeiro_mainmenu
        '
        Me.LoadivNeiro_mainmenu.Name = "LoadivNeiro_mainmenu"
        resources.ApplyResources(Me.LoadivNeiro_mainmenu, "LoadivNeiro_mainmenu")
        '
        'LoadivGist_mainmenu
        '
        Me.LoadivGist_mainmenu.Name = "LoadivGist_mainmenu"
        resources.ApplyResources(Me.LoadivGist_mainmenu, "LoadivGist_mainmenu")
        '
        'TEOcriteria_mainmenu
        '
        Me.TEOcriteria_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.TEOcritPrice_mainmenu, Me.TEOcritRemont_mainmenu, Me.TEOcritBezop_mainmenu, Me.TEOcritDegrad_mainmenu})
        Me.TEOcriteria_mainmenu.Name = "TEOcriteria_mainmenu"
        resources.ApplyResources(Me.TEOcriteria_mainmenu, "TEOcriteria_mainmenu")
        '
        'TEOcritPrice_mainmenu
        '
        Me.TEOcritPrice_mainmenu.Name = "TEOcritPrice_mainmenu"
        resources.ApplyResources(Me.TEOcritPrice_mainmenu, "TEOcritPrice_mainmenu")
        '
        'TEOcritRemont_mainmenu
        '
        Me.TEOcritRemont_mainmenu.Name = "TEOcritRemont_mainmenu"
        resources.ApplyResources(Me.TEOcritRemont_mainmenu, "TEOcritRemont_mainmenu")
        '
        'TEOcritBezop_mainmenu
        '
        Me.TEOcritBezop_mainmenu.Name = "TEOcritBezop_mainmenu"
        resources.ApplyResources(Me.TEOcritBezop_mainmenu, "TEOcritBezop_mainmenu")
        '
        'TEOcritDegrad_mainmenu
        '
        Me.TEOcritDegrad_mainmenu.Name = "TEOcritDegrad_mainmenu"
        resources.ApplyResources(Me.TEOcritDegrad_mainmenu, "TEOcritDegrad_mainmenu")
        '
        'PlanTER_mainmenu
        '
        Me.PlanTER_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.PrognosCalc_mainmenu, Me.TERReport_mainmenu})
        Me.PlanTER_mainmenu.Name = "PlanTER_mainmenu"
        resources.ApplyResources(Me.PlanTER_mainmenu, "PlanTER_mainmenu")
        '
        'PrognosCalc_mainmenu
        '
        Me.PrognosCalc_mainmenu.Name = "PrognosCalc_mainmenu"
        resources.ApplyResources(Me.PrognosCalc_mainmenu, "PrognosCalc_mainmenu")
        '
        'TERReport_mainmenu
        '
        Me.TERReport_mainmenu.Name = "TERReport_mainmenu"
        resources.ApplyResources(Me.TERReport_mainmenu, "TERReport_mainmenu")
        '
        'Help_mainmenu
        '
        Me.Help_mainmenu.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.ОПрограммеToolStripMenuItem, Me.РазработчикиToolStripMenuItem})
        Me.Help_mainmenu.Name = "Help_mainmenu"
        resources.ApplyResources(Me.Help_mainmenu, "Help_mainmenu")
        '
        'ОПрограммеToolStripMenuItem
        '
        Me.ОПрограммеToolStripMenuItem.Name = "ОПрограммеToolStripMenuItem"
        resources.ApplyResources(Me.ОПрограммеToolStripMenuItem, "ОПрограммеToolStripMenuItem")
        '
        'РазработчикиToolStripMenuItem
        '
        Me.РазработчикиToolStripMenuItem.Name = "РазработчикиToolStripMenuItem"
        resources.ApplyResources(Me.РазработчикиToolStripMenuItem, "РазработчикиToolStripMenuItem")
        '
        'Open_raschet
        '
        resources.ApplyResources(Me.Open_raschet, "Open_raschet")
        '
        'Label1
        '
        resources.ApplyResources(Me.Label1, "Label1")
        Me.Label1.BackColor = System.Drawing.Color.Transparent
        Me.Label1.ForeColor = System.Drawing.Color.Gold
        Me.Label1.Name = "Label1"
        '
        'Label2
        '
        resources.ApplyResources(Me.Label2, "Label2")
        Me.Label2.BackColor = System.Drawing.Color.Transparent
        Me.Label2.ForeColor = System.Drawing.Color.Gold
        Me.Label2.Name = "Label2"
        '
        'Open_TEO_base
        '
        Me.Open_TEO_base.FileName = "OpenFileDialog1"
        resources.ApplyResources(Me.Open_TEO_base, "Open_TEO_base")
        '
        'Save_raschet
        '
        resources.ApplyResources(Me.Save_raschet, "Save_raschet")
        '
        'Save_TEO_base
        '
        resources.ApplyResources(Me.Save_TEO_base, "Save_TEO_base")
        '
        'Open_pl_prof_vsp_base
        '
        resources.ApplyResources(Me.Open_pl_prof_vsp_base, "Open_pl_prof_vsp_base")
        '
        'Open_gist_force
        '
        Me.Open_gist_force.DefaultExt = "gst,mdb"
        resources.ApplyResources(Me.Open_gist_force, "Open_gist_force")
        '
        'MainForm
        '
        resources.ApplyResources(Me, "$this")
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackgroundImage = Global.neiroexpert.My.Resources.Resources.psi
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.MenuStrip1)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        Me.MainMenuStrip = Me.MenuStrip1
        Me.Name = "MainForm"
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents File_mainmenu As ToolStripMenuItem
    Friend WithEvents Openraschet_mainmenu As ToolStripMenuItem
    Friend WithEvents Saveraschet_mainmenu As ToolStripMenuItem
    Friend WithEvents OpenTEObase_mainmenu As ToolStripMenuItem
    Friend WithEvents SaveTEObase_mainmenu As ToolStripMenuItem
    Friend WithEvents WayStruct_mainmenu As ToolStripMenuItem
    Friend WithEvents Ekspluslov_mainmenu As ToolStripMenuItem
    Friend WithEvents Prognose_mainmenu As ToolStripMenuItem
    Friend WithEvents Help_mainmenu As ToolStripMenuItem
    Friend WithEvents Loadiv_mainmenu As ToolStripMenuItem
    Friend WithEvents LoadivNeiro_mainmenu As ToolStripMenuItem
    Friend WithEvents LoadivGist_mainmenu As ToolStripMenuItem
    Friend WithEvents TEOcriteria_mainmenu As ToolStripMenuItem
    Friend WithEvents PlanTER_mainmenu As ToolStripMenuItem
    Friend WithEvents TEOcritPrice_mainmenu As ToolStripMenuItem
    Friend WithEvents TEOcritRemont_mainmenu As ToolStripMenuItem
    Friend WithEvents TEOcritBezop_mainmenu As ToolStripMenuItem
    Friend WithEvents PrognosCalc_mainmenu As ToolStripMenuItem
    Friend WithEvents TERReport_mainmenu As ToolStripMenuItem
    Friend WithEvents ОПрограммеToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents РазработчикиToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents PlanProf_mainmenu As ToolStripMenuItem
    Friend WithEvents VSP_mainmenu As ToolStripMenuItem
    Friend WithEvents Vagonpotok_mainmenu As ToolStripMenuItem
    Friend WithEvents Climat_mainmenu As ToolStripMenuItem
    Friend WithEvents Open_raschet As OpenFileDialog
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents TEOcritDegrad_mainmenu As ToolStripMenuItem
    Friend WithEvents Open_TEO_base As OpenFileDialog
    Friend WithEvents Save_raschet As SaveFileDialog
    Friend WithEvents Save_TEO_base As SaveFileDialog
    Friend WithEvents Open_WayStruct_Base_mainmenu As ToolStripMenuItem
    Friend WithEvents Open_pl_prof_vsp_base As OpenFileDialog
    Friend WithEvents Open_gist_force As OpenFileDialog
    Friend WithEvents LoadivVeip_mainmenu As ToolStripMenuItem
End Class
