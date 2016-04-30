var data = undefined;
try {
	eval('data={"code":{"codeId":10111,"status":2,"spaceType":1,"isNeedCloseButton":true,"enablePcPicPlus":true,"enableMobPicPlus":true,"enableMobDuBao":true,"isNeedScreenAD":false,"bcode":{"mob":"u2551539","pc":"u2551540","mobScreen":"u2359167","pc3_2":"u2570368","pcPicPlus":"u2583102","mobPicPlus":"","mobDuBao":""}},"referer":"http://blog.sina.com.cn/s/articlelist_1195883527_0_2.html","apGroupId":"","apTagId":"","w":580,"h":88,"clid":"00:14:4f:46:2c:86","apmac":"00:14:4f:46:2c:86","onlyyn":false,"chooseName":"baidu","isScreenAD":false}');
} catch (error) {
	console.log(error);
}
if(data.code){
	if(data.code.bcode){
		data.code.baiduCodeId = data.code.bcode.mob;
		data.code.baiduPCCodeId = data.code.bcode.pc;
		data.code.baiduScreenADCodeId = data.code.bcode.mobScreen;
	}
	var space = window.ynspace;
	if(space){
		for(var i=0; i<space.length; i++){
			if(space[i].id == data.code.codeId){
				space[i].ynwf.createAd(data);
				break;
			}
		}
	}else{
		window.ynmap.get(data.code.codeId).createAd(data);
	}
}

