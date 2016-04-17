# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import json
from Statistics import Statistics
__author__="panos"
__date__ ="$Apr 8, 2016 1:29:59 PM$"

class cntdt:

    #data = '[{"stats": {"mem_perc": "2.31", "cpu_perc": "0.32", "net_rx_MB": 268.8, "block_in_MB": 16.4, "mem_limit_MB": 1042.0, "block_ou_MB": 10.4, "mem_usage_MB": 24.06, "net_tx_MB": 5005.0, "id": "5667d936cd47"}, "name": ["/sick_mcnulty"], "created": 1459962582, "image": "sha256:1d7584d6d6249ae7b7a658dbd8422d927e24b6bce1e073c0a263de9bd19b15e0", "image_name": "nodecollector", "id": "5667d936cd47757ed845190edae93a2b7475318c9cf21f2e6eacb50f529a6b75"}, {"stats": {"mem_perc": "0.84", "cpu_perc": "0.00", "net_rx_MB": 9878.0, "block_in_MB": 39.94, "mem_limit_MB": 1042.0, "block_ou_MB": 0.0, "mem_usage_MB": 8.757, "net_tx_MB": 469.5, "id": "43b75f243cfa"}, "name": ["/nostalgic_golick"], "created": 1459853803, "image": "sha256:ba2bb23371961d46d174b94f5bed54912cdc0c84b6b4d41f83e003dde895699e", "image_name": "prom/pushgateway", "id": "43b75f243cfa077d40febb8ba6d0754e5407b2558abdaa7ae4c232b3b5c2ad78"}, {"stats": {"mem_perc": "0.24", "cpu_perc": "0.01", "net_rx_MB": 5.61, "block_in_MB": 26.44, "mem_limit_MB": 1042.0, "block_ou_MB": 0.0, "mem_usage_MB": 2.527, "net_tx_MB": 116.3, "id": "6de197661fa7"}, "name": ["/adoring_mccarthy"], "created": 1459789382, "image": "sha256:d9b93c3559e93976756ba6cc14c4ccbfef6309b463678d25fb881d5faf51f5af", "image_name": "prom/node-exporter", "id": "6de197661fa769497d25b1a8d527bc7c952ca01d2243a163ee4cb317c0708763"}, {"stats": {"mem_perc": "2.73", "cpu_perc": "1.16", "net_rx_MB": 37.84, "block_in_MB": 77.55, "mem_limit_MB": 1042.0, "block_ou_MB": 0.0, "mem_usage_MB": 28.47, "net_tx_MB": 769.8, "id": "5761a9fd062d"}, "name": ["/awesome_wozniak"], "created": 1459783584, "image": "sha256:a56e3f67a48db8517802c166eebcafa298b975b8f9f4dca0893f21808284ba48", "image_name": "google/cadvisor:latest", "id": "5761a9fd062d126ddecbe36d8787a65c4fe2fba1d565711fe67b40113d040701"}]'
    data = []
    
    def __init__(self):
        test =1
        #return self.prom_parser(json.loads(self.data))
        self.data = Statistics().getMonInfo()

    def checkNone(self,val_):
	if val_ == None:
		return 0
        return val_
        
    def prom_parser(self):
        #containers metric types
        cnt_created = "# TYPE cnt_created count" + '\n'
        cnt_cpu_perc = "# TYPE cnt_cpu_perc gauge" + '\n'
        cnt_mem_perc = "# TYPE cnt_mem_perc gauge" + '\n'
        cnt_mem_usage_MB = "# TYPE cnt_mem_usage_MB gauge" + '\n'
        cnt_mem_limit_MB = "# TYPE cnt_mem_limit_MB gauge" + '\n'
        cnt_net_rx_MB = "# TYPE cnt_net_rx_MB gauge" + '\n'
        cnt_net_tx_MB = "# TYPE cnt_net_tx_MB gauge" + '\n'
        cnt_block_in_MB = "# TYPE cnt_block_in_MB gauge" + '\n'
        cnt_block_ou_MB = "# TYPE cnt_block_ou_MB gauge" + '\n'
	
        for cnt in self.data:
            cnt_created = "cnt_created{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}" +str(self.checkNone(cnt['created']))+ '\n'
            cnt_cpu_perc += "cnt_cpu_perc{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}"+str(self.checkNone(cnt['stats']['cpu_perc']))+ '\n'
            cnt_mem_perc += "cnt_mem_perc{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}"+str(self.checkNone(cnt['stats']['mem_perc']))+ '\n'
            cnt_mem_usage_MB += "cnt_mem_usage_MB{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}"+str(self.checkNone(cnt['stats']['mem_usage_MB']))+ '\n'
            cnt_mem_limit_MB += "cnt_mem_limit_MB {id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}" +str(self.checkNone(cnt['stats']['mem_limit_MB']))+ '\n'
            cnt_net_rx_MB += "cnt_net_rx_MB{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}" +str(self.checkNone(cnt['stats']['net_rx_MB']))+ '\n'
            cnt_net_tx_MB += "cnt_net_tx_MB{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}" +str(self.checkNone(cnt['stats']['net_tx_MB']))+ '\n'
            cnt_block_in_MB += "cnt_block_in_MB{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}" +str(self.checkNone(cnt['stats']['block_in_MB']))+ '\n'
            cnt_block_ou_MB += "cnt_block_ou_MB{id=\""+cnt['id']+"\",image_name=\""+cnt['image_name']+"\",image=\""+cnt['image']+"\"}" +str(self.checkNone(cnt['stats']['block_ou_MB']))+ '\n'
            
        data = cnt_cpu_perc +cnt_mem_perc + cnt_mem_usage_MB + cnt_mem_limit_MB + cnt_net_rx_MB + cnt_net_tx_MB + cnt_block_in_MB + cnt_block_ou_MB
	return data
