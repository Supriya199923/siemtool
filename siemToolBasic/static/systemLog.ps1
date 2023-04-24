  $logs = Get-EventLog -LogName System -Newest 20
  foreach($log in $logs)
  {
    $timestamp_ms = $log.TimeWritten.DateTime
    $entryt=$log.EntryType.ToString()
    #$epoch = New-Object DateTime(1970, 1, 1, 0, 0, 0, [DateTimeKind]::Utc)
    #$dt = $epoch.AddMilliseconds($timestamp_ms)
    $log | Add-Member -MemberType NoteProperty -Name "TimeWrittenAsDate" -Value $timestamp_ms
    $log | Add-Member -MemberType NoteProperty -Name "EntryTypeAsString" -Value $entryt
  }
  #$event =  $logs | Select-Object index,timewritten,machinename,EntryType,InstanceId,TimeWrittenUnix,entryTString | ConvertTo-Json
  $event =  $logs |Select-Object Index,TimeWritten,MachineName,EntryType,InstanceId,TimeWrittenAsDate,EntryTypeAsString | ConvertTo-Json
  return $event
