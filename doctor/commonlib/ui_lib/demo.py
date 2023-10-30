import requests

url = "https://kibana.test.sensenova.cn/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true"

payload = "{\"index\":\"logging*\",\"ignore_unavailable\":true,\"preference\":1693978929737}\n{\"timeout\":\"30000ms\",\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"fixed_interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[],\"filter\":[{\"bool\":{\"filter\":[{\"multi_match\":{\"type\":\"phrase\",\"query\":\"7ea07d90-30d2-4013-86fb-9517c6064f23\",\"lenient\":true}},{\"multi_match\":{\"type\":\"phrase\",\"query\":\"GetRoutedModel\",\"lenient\":true}}]}},{\"range\":{\"@timestamp\":{\"format\":\"strict_date_optional_time\",\"gte\":\"2023-08-30T06:31:20.347Z\",\"lte\":\"2023-09-06T06:31:20.347Z\"}}}],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\n"
headers = {
  'authority': 'kibana.test.sensenova.cn',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'content-type': 'application/x-ndjson',
  'kbn-version': '7.4.2',
  'origin': 'https://kibana.test.sensenova.cn',
  'referer': 'https://kibana.test.sensenova.cn/app/kibana',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
  'Cookie': 'sid=Fe26.2**ef9afca4db0d1a286d0906d16e35a5ff3a077b0170d75e9a449527c5f12835bd*KlzKccAWna23xu0YGkwmIA*TtnS8TPAuhoypVNLsZvT9rghlTHFmr_O1Jvf-vPnszn8cGQKlVlNZQ0qIisk2kXoieDPPIBPogTpFNPHQC3i9u200ivIe3OW0gBfWlE4lBtIf9Sjew8CTDSCXNyN3ocr**c3ee7b9165c910635a47bc04b42267628141db73b317575910c738595e5a5971*G503CZh1Tv_rVNNuT8BJk4-hzkSyam-OX5gWWdc1r9Q'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
