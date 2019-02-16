Public Class MainForm
    Private Sub ИсходныеДыанToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles TEOcriteria_mainmenu.Click

    End Sub

    Private Sub ПрогнозированиеToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles Prognose_mainmenu.Click

    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub ЭксплуатацонныеToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles Ekspluslov_mainmenu.Click

    End Sub

    Private Sub ПутеваяИнфраструктураToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles WayStruct_mainmenu.Click

    End Sub

    Private Sub MenuStrip1_ItemClicked(sender As Object, e As ToolStripItemClickedEventArgs) Handles MenuStrip1.ItemClicked

    End Sub

    Private Sub ПланпрофильПутиToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles PlanProf_mainmenu.Click
        Plan_prof.Show()
    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles Label2.Click

    End Sub

    Private Sub ЗагрузитьРасчетToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles Openraschet_mainmenu.Click
        Open_raschet.ShowDialog()
    End Sub

    Private Sub СохратьРасчетToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles Saveraschet_mainmenu.Click
        Save_raschet.ShowDialog()
    End Sub

    Private Sub ЗагрузитьБазуИсходныхДанныхToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles OpenTEObase_mainmenu.Click
        Open_TEO_base.ShowDialog()
    End Sub

    Private Sub СохранитьБазуИсходныхДанныхToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles SaveTEObase_mainmenu.Click
        Save_TEO_base.ShowDialog()
    End Sub

    Private Sub КоэффициентыДеградационныхКривыхToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles TEOcritDegrad_mainmenu.Click
        IntensDegrad_Form.Show()
    End Sub

    Private Sub ПовреждаемостьToolStripMenuItem_Click(sender As Object, e As EventArgs)
        IntensDegrad_Form.Show()
    End Sub

    Private Sub MainForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub VSP_mainmenu_Click(sender As Object, e As EventArgs) Handles VSP_mainmenu.Click
        VSP_input.Show()
    End Sub

    Private Sub ЗагрузкаБазДанныхХарактеристикПутиЕКАСУИАСУПИДрToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles Open_WayStruct_Base_mainmenu.Click
        Open_pl_prof_vsp_base.ShowDialog()
    End Sub

    Private Sub Open_pl_prof_vsp_base_FileOk(sender As Object, e As System.ComponentModel.CancelEventArgs) Handles Open_pl_prof_vsp_base.FileOk

    End Sub

    Private Sub LoadivGist_mainmenu_Click(sender As Object, e As EventArgs) Handles LoadivGist_mainmenu.Click
        Open_gist_force.ShowDialog()
    End Sub

    Private Sub РазработчикиToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles РазработчикиToolStripMenuItem.Click

    End Sub

    Private Sub РасчетНагруженностиПоМоделиВЭИПToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles LoadivVeip_mainmenu.Click
        Vivod_Loadiv.Show()
    End Sub

    Private Sub Loadiv_mainmenu_Click(sender As Object, e As EventArgs) Handles Loadiv_mainmenu.Click

    End Sub

    Private Sub LoadivNeiro_mainmenu_Click(sender As Object, e As EventArgs) Handles LoadivNeiro_mainmenu.Click
        Vivod_Loadiv.Show()
    End Sub

    Private Sub Vagonpotok_mainmenu_Click(sender As Object, e As EventArgs) Handles Vagonpotok_mainmenu.Click
        VagPoezdPotok.Show()
    End Sub

    Private Sub ВыходAltXToolStripMenuItem_Click(sender As Object, e As EventArgs)
        Close()
    End Sub

    Private Sub PrognosCalc_mainmenu_Click(sender As Object, e As EventArgs) Handles PrognosCalc_mainmenu.Click
        Strategy.Show()
    End Sub
End Class
