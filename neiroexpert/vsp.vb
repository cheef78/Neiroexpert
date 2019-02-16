Public Class plan_prof
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub GroupBox1_Enter(sender As Object, e As EventArgs) Handles GroupBox1.Enter

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Hide()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Hide()
    End Sub

    Private Sub TabPlan_Click(sender As Object, e As EventArgs) Handles TabPlan.Click

    End Sub

    Private Sub Label6_Click(sender As Object, e As EventArgs) Handles Label6.Click

    End Sub

    Private Sub R_1500_TextChanged(sender As Object, e As EventArgs) Handles R_1500.TextChanged

    End Sub

    Private Sub TextBox7_TextChanged(sender As Object, e As EventArgs) Handles H_10000.TextChanged

    End Sub

    Private Sub TextBox2_TextChanged(sender As Object, e As EventArgs) Handles H_275.TextChanged

    End Sub

    Private Sub ShK_10000_TextChanged(sender As Object, e As EventArgs) Handles ShK_10000.TextChanged

    End Sub

    Private Sub ShK_500_TextChanged(sender As Object, e As EventArgs) Handles ShK_500.TextChanged

    End Sub

    Private Sub RadioButton2_CheckedChanged(sender As Object, e As EventArgs) Handles pl_file_base_butt.CheckedChanged
        If pl_file_base_butt.Checked = True Then
            open_plbase_butt.Enabled = True
            Tab_PL_H_SHK_Prof.Enabled = False
        Else
            open_plbase_butt.Enabled = False
            Tab_PL_H_SHK_Prof.Enabled = True
        End If



    End Sub

    Private Sub Label27_Click(sender As Object, e As EventArgs) Handles Label27.Click

    End Sub

    Private Sub TextBox6_TextChanged(sender As Object, e As EventArgs) Handles I_min10.TextChanged

    End Sub

    Private Sub TabPrf_Click(sender As Object, e As EventArgs) Handles TabPrf.Click

    End Sub

    Private Sub Label22_Click(sender As Object, e As EventArgs) Handles Label22.Click

    End Sub

    Private Sub ShK_1500_TextChanged(sender As Object, e As EventArgs) Handles ShK_1500.TextChanged

    End Sub

    Private Sub ShK_900_TextChanged(sender As Object, e As EventArgs) Handles ShK_900.TextChanged

    End Sub

    Private Sub ShK_325_TextChanged(sender As Object, e As EventArgs) Handles ShK_325.TextChanged

    End Sub

    Private Sub pl_udel_butt_CheckedChanged(sender As Object, e As EventArgs) Handles pl_udel_butt.CheckedChanged
        If pl_udel_butt.Checked = True Then
            open_plbase_butt.Enabled = False
            Tab_PL_H_SHK_Prof.Enabled = True
        Else
            open_plbase_butt.Enabled = True
            Tab_PL_H_SHK_Prof.Enabled = False
        End If


    End Sub

    Private Sub OpenFileDialog1_FileOk(sender As Object, e As System.ComponentModel.CancelEventArgs) Handles Open_pl_prof_base.FileOk

    End Sub

    Private Sub open_plbase_butt_Click(sender As Object, e As EventArgs) Handles open_plbase_butt.Click
        Open_pl_prof_base.ShowDialog()
    End Sub
End Class