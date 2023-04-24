 $logs = Get-EventLog -LogName Security -Newest 80
  foreach($log in $logs)
  {
    $timestamp_ms = $log.TimeWritten.DateTime
    $entryt=$log.EntryType.ToString()

    $log | Add-Member -MemberType NoteProperty -Name "TimeWrittenAsDate" -Value $timestamp_ms
    $log | Add-Member -MemberType NoteProperty -Name "EntryTypeAsString" -Value $entryt
  }
  $event =  $logs |Select-Object Index,TimeWritten,MachineName,EntryType,InstanceId,TimeWrittenAsDate,EntryTypeAsString | ConvertTo-Json
  return $event