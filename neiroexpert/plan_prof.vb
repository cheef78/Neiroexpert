Public Class Plan_prof
    Public Sub Data_plan_prof()

        'Обявляем и считываем массив долей радиусов

        Dim Radius(6) As Integer
        Radius(0) = Me.R_10000.Text
        Radius(1) = Me.R_1500.Text
        Radius(2) = Me.R_900.Text
        Radius(3) = Me.R_500.Text
        Radius(4) = Me.R_325.Text
        Radius(5) = Me.R_275.Text
        Radius(6) = Me.R_225.Text

        'Обявляем и считываем массив возвышений для радиусов

        Dim H(6) As Integer
        H(0) = Me.H_10000.Text
        H(1) = Me.R_1500.Text
        H(2) = Me.H_900.Text
        H(3) = Me.H_500.Text
        H(4) = Me.H_325.Text
        H(5) = Me.H_275.Text
        H(6) = Me.H_225.Text

        'Обявляем и считываем массив нормативов ширины колеи

        Dim ShK(6) As Integer
        ShK(0) = Me.ShK_10000.Text
        ShK(1) = Me.ShK_1500.Text
        ShK(2) = Me.ShK_900.Text
        ShK(3) = Me.ShK_500.Text
        ShK(4) = Me.ShK_325.Text
        ShK(5) = Me.ShK_275.Text
        ShK(6) = Me.ShK_225.Text



    End Sub

    Protected Overrides Sub Finalize()
        MyBase.Finalize()
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub GroupBox1_Enter(sender As Object, e As EventArgs)

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



    Private Sub OpenFileDialog1_FileOk(sender As Object, e As System.ComponentModel.CancelEventArgs)

    End Sub


End Class