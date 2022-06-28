# pc端钉钉申请的token
dingding_token = ""           # 必填
# ---- 区块浏览器申请的apikey ----
apikey_FTM = ""               #必填
apikey_MATIC = ""             #必填
apikey_BSC = ""               #必填
apikey_ETH = "8TJHIA2SDNWT1KC13MX2Z4F8SCY2IJNXF2"               #必填
apikey_AVAX = ""              #必填

# 填写需要监控的地址
oxdata = {
    # "0xdAC17F958D2ee523a2206206994597C13D831ec7": "FTM",
    "0x00192Fb10dF37c9FB26829eb2CC623cd1BF599E8":"mint",
    "0xD120C8B14A5D217b8063ADA404c19743f3e18A36":"模板地址",
    "0xbee558b39985eafc9c0e531de748968f38dd3421":"微博:比特肥",
    "0xb35b90e03f5d7dbd746914ee7e7eda8647cb3a14":"微博:某圈葫芦娃",
    "0xf916719c7251e109cf3d1a977b6cad198b630c32":"推特:MoonNFT6",
    "0x113d754ff2e6ca9fd6ab51932493e4f9dabdf596":"🤹🏻‍♂️.eth",
    "0x361d4da8936c19100cc7643faefbad2632f7e321":"微博:ChrisZCT",
    "0x8eef779818afa953b0652e45438423ebe089f55a":"微博:nft毒奶",
    "0x1af331dc34dd7c5c62af28b5685328318b61888a":"微博:LaserCat",
    "0x718c51a7e72b4a90b5e43a0b2b35adba0913540d":"微博:牛顿布莱尼兹公式",
    "0xd7f4e01b66bedde8aa85300130cc6c7b9823942c":"微博:0xace",
    "0x667566c500a0d40b1fdce38af3a756a7f45d81e0":"403.eth",
    "0x6f9f3bc055c5f86972e45588a610349824f69ee1":"微博:uniswap",
    "0x2480f754530776cfe59bbf26776345ab370ee36a":"微博:puredee_投资逻辑",
    "0x7ef61cacd0c785eacdfe17649d1c5bcba676a858":"推特:itsyoboymoe",
    "0xc665a60f22dda926b920deb8ffac0ef9d8a17460":"mikegee",
    "0xef3f063136fe5002065bf7c4a2d85ff34cfb0ac0":"pickleric.eth",
    "0x5be8f739c8ea94d99b44ab0b1421889c8b99b2e1":"推特trebooomin",
    "0x3f3e2f43f0ac69f30ec38d3e4fec304bdf330e7a":"推特RelicCK",
    "0x5b20783f4bAaBd33BB53DD77C9B0459f5701E36A":"推特PrepsToThePros",
    '0x081591764a13e72aeb6bed098e7da34063ea8ac4':'QualityBlockNFT',
    "0xc57b2900f3ab9b9bd4ffcdb8174cd7665d0da8bc":"BunchuBets",
    "0x86a41524cb61edd8b115a72ad9735f8068996688":"推特mattcrypted",
    "0x7c121489e50e6672bbb59cc4c3fc86eaa8fb8364":"推特jRSomething_",
    "0xd5a771da32a392036a98f7da6b11d46d6d1c61f9":"推特SLAddictNFT",
    "0x442dccee68425828c106a3662014b4f131e3bd9b":"推特j1mmyeth",
    "0x6186290b28d511bff971631c916244a9fc539cfe":"推特Barthazian",
    "0x083a1457d8fc367c664b59886d651910fb9e9a70":"推特:饭团哥",
    "0xfC12468e069fDCE70A2d2D27e9ED47eBb87e77aC":"来来BTC",
}
#接收方的智能合约地址，方便查阅
contract_list = {
    "0x10ed43c718714eb63d5aa57b78b54704e256024e":"pancake routerV2",
    "0x95c78222b3d6e262426483d42cfa53685a67ab9d":"Venus: vBUSD Token",
    "0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31":"Metamask: Swap Router",
    "0xe9e7cea3dedca5984780bafc599bd69add087d56":"Binance: BUSD Stablecoin",
    "0x8f8dd7db1bda5ed3da8c9daf3bfa471c12d58486":"Dodoex: V2 Proxy",
    "0x7be8076f4ea4a4ad08075c2508e481d6c946d12b":"Opensea"
}
# 当前transfer的方式
method_data = {
    "0x095ea7b3":"Approve",
    "0x7ff36ab5":"Swap Exact ETH For Tokens",
    "0x18cbafe5":"Swap Exact Token For ETH",
    "0x":"Transfer",
    "0xf305d719":"Add Liquiity ETH",
    "0xfb3bdb41":"Swap ETH For Exact Tokens",
    "0xa22cb465":"setApprovalForAll",
    "0xab834bab":"atomicMatch_(buy_nft)"
}