$CSVSQL = {param([string[]]$tbl ,[string[]]$sql )
$cnnect = "Data Source=SQL_SERVER_ADDRESS; Integrated Security=SSPI; Initial Catalog=SQL_DATABASE_NAME"
$xcl = "C:\Users\***\LOAD_PY\"
$provider = "Provider=Microsoft.ACE.OLEDB.12.0; Data Source=$xcl;Extended Properties=" + "`"Text;HDR=Yes`""
$olec = new-object system.data.oledb.oledbconnection($provider)
$cmd = new-object system.data.oledb.oledbcommand($sql)
$cmd.connection = $olec
$olec.Open()
$reader = $cmd.ExecuteReader()
$sqlbk = new-object System.Data.SqlClient.SqlBulkCopy($cnnect)
$sqlbk.DestinationTablename = $tbl
$sqlbk.BulkCopyTimeout = 0
$sqlbk.WriteToServer($reader)
}


$ExSQLfile = {param([string[]]$file)
$cnnect = "Data Source=SQL_SERVER_ADDRESS; Integrated Security=SSPI; Initial Catalog=SQL_DATABASE_NAME"
$cmnd = [IO.File]::ReadAllText($file)
$cnnection = new-object system.data.sqlclient.sqlconnection($cnnect)
$cmmnd = new-object system.data.sqlclient.sqlcommand($cmnd)
$cmmnd.connection=$cnnection
$cmmnd.CommandTimeout = 0
$cnnection.Open()
$res = $cmmnd.ExecuteNonQuery()
}

$ExSQLstring = {param([string[]]$cmnd)
$cnnect = Data Source=SQL_SERVER_ADDRESS; Integrated Security=SSPI; Initial Catalog=SQL_DATABASE_NAME"
$cnnection = new-object system.data.sqlclient.sqlconnection($cnnect)
$cmmnd = new-object system.data.sqlclient.sqlcommand($cmnd)
$cmmnd.connection=$cnnection
$cmmnd.CommandTimeout = 0
$cnnection.Open()
$res = $cmmnd.ExecuteNonQuery()
}


function W {
Invoke-Command -ScriptBlock $ExSQLstring -ArgumentList "DELETE FROM [SQL_DATABASE_NAME].[dbo].[temp_temp]"
$Job = Start-Job $CSVSQL -ArgumentList "dbo.temp_temp", "SELECT * FROM [W_NEW.csv]" -RunAs32
$SCStore = $Job | Wait-Job | Receive-Job
$SCStore = $Job | Wait-Job | Receive-Job
Write-Host "WEEKLY DATA LOADED"
Write-Host "WEEKLY DATA TRANSFORMED"
Write-Host "WEEKLY DATA LOAD EXECUTED"

}
