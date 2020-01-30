<?php
  $key = 'your_public_key';
  $secert = 'your_secret_key';
  $returnData = '[{"your_field_1": "field 1 value","your_field_2": "field 2 value"}]';
  $compressed = gzcompress(utf8_encode([$returnData]));
  $secert = hex2bin($secert);
  $sign = hash_hmac('sha256', $compressed, $secert, true);
  $sign = utf8_decode(bin2hex($sign));
  $curl = curl_init();
  curl_setopt_array($curl, array(
    CURLOPT_URL => "https://connect-sbx.dispatch.me/agent/in",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 0,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_POSTFIELDS => $compressed,
    CURLOPT_HTTPHEADER => array(
        "Content-Type: application/json",
        "RecordType: job",
        "X-Dispatch-Key: $key",
        "X-Dispatch-Signature: $sign"
    ),
  ));
  $response = curl_exec($curl);
  curl_close($curl);
  echo $response;
