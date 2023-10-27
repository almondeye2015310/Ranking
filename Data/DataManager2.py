
# coding: UTF-8
import json
from pathlib import Path

data = """
【80】McKinsey&Company GoldmanSachs MorganStanley
【79】BostonConsultingGroup*BCG* Bain&Company JPMorgan BankofAmerica
=====スーパーエリート=====
【78】ATKearney Citi Lazard Google
【77】PwC(Strategy&) UBS DeutscheBank Barclays GSAM JPMorgan(AM) UBS(AM) Fidelity 
【76】RolandBerger ArthurD.Little*ADL* L.E.K. OliverWyman 野村證券(GM) DWS BlackRock
=====海外トップ大勝ち=====
【75】ZSAssociates BNPParibas 野村証券(IB) SMBC日興証券(IB)
【74】Simon-Kucher HoulihanLokey SociétéGénérale CréditAgricole HSBC みずほ証券(IB/GM) WellsFargo 三菱商事 日本銀行(総合職)
【73】日興アセットマネジメント 三井物産 伊藤忠商事 三菱地所 三井不動産 日本政策投資銀行*DBJ* 東京海上日動(SPEC) P&G(マーケ)
【72】EYParthenon Accenture(戦略) KornFerry KPMG(FAS) 三菱UFJモルガンスタンレー証券(IB) 野村アセットマネジメント(運用) 東京海上アセットマネジメント 講談社 集英社 小学館 医学書院 テレビ朝日 TBS 日本生命(AC) 第一生命(AC) Microsoft Cisco
【71】経営共創基盤*IGPI* ドリームインキュベータ*DI* コーポレイトディレクション*CDI* 野村総合研究所*NRI*(経営) SMBC日興証券(GM) 三菱UFJモルガンスタンレー証券(GM) 大和証券(GM) 野村アセットマネジメント(マーケ) 三井住友DSアセットマネジメント(運用) ※農林中央金庫(GI) ※年金積立金管理運用独立行政法人*GPIF* 住友商事 日本テレビ 白泉社 文藝春秋 Bloomberg EY新日本(AC) PwCあらた(AC) 損害保険ジャパン(AC) みずほFG(GCF/GM&AM) 三井住友海上(スペシフィック) Amazon(Consumer) AmazonWebServices*AWS* 地主*日本商業開発*
【70】PwCアドバイザリー YCPSolidiance 三菱総合研究所*MRI* 大和証券(IB) 野村アセットマネジメント(ビジマネ) アセットマネジメントOne 日本生命(資産運用) 丸紅 ヒューリック 日経BP 電通 日本経済新聞 フジテレビ 国際協力銀行*JBIC* 三菱UFJ銀行(戦略財務会計) その他アクチュアリー全般 VMware ユニリーバ(マーケ) USJ(マーケ) Mercer 日本取引所グループ 国際協力機構*JICA* JAFCO
=====東京一工勝ち=====
【69】アビーム(戦略) B&DX AAIC 日本経営システム P&Eディレクションズ JR東海 三菱UFJ銀行(グローバル) テレビ東京 読売テレビ 朝日放送テレビ 毎日放送 関西テレビ マガジンハウス 日本ロレアル(マーケ) 三井住友DSアセットマネジメント(運用以外)
【68】デロイトトーマツコンサルティング*DTC* PwCコンサルティング 日本IBM(戦略) 三菱UFJリサーチ&コンサルティング*MURC*  大和アセットマネジメント 三菱UFJ国際投信 日本郵船 東京ガス 朝日新聞 新潮社 東洋経済新報 東急不動産 花王(マーケ) 資生堂(マーケ) 
=====早慶地帝優秀層勝ち=====
【67】Accenture(DDC) KPMGコンサルティング デロイトトーマツファイナンシャルアドバイザリー*DTFA* 日本総合研究所*JRI*(コンサル) CambridgeTechnologyPartners SAP 任天堂 商船三井 国際石油開発帝石*INPEX* ケネディクス 監査法人トーマツ PwCあらた EY新日本 あずさ ユニ・チャーム(マーケ) 森ビル 東京建物 森トラスト 共同通信 博報堂
【66】Accenture(ビジネス/デジタル) EYストラテジーアンドコンサルティング 三菱ufj銀行(システム/デジタル) 三菱ufj銀行(ウェルマネ)農林中央金庫 野村総合研究所*NRI*(AE/TE) ソニーグループ Salesforce 味の素 キーエンス 大阪ガス テレビ大阪 日本貿易振興機構 りそな銀行(専門職コース) ニッセイアセットマネジメント 三井住友トラストアセットマネジメント NHK 豊田通商 双日 伊藤忠丸紅鉄鋼 野村不動産 住友不動産
【65】日本IBM(コンサル) アビームコンサルティング 日本Oracle Capgemini P&G(マーケ以外) トヨタ サントリー 富士フイルム 川崎汽船 阪急阪神HD 関西電力 ENEOS JERA JT 三菱UFJ銀行(OP) 東京海上日動(グローバル) 東京中小企業投資育成*SBIC* レオス・キャピタルワークス東急 武田薬品工業 ファナック 東宝 松竹 NTT都市開発 KADOKAWA 日本中央競馬会*JRA* 明治大学(職員) スマートニュース 読売新聞
【64】みずほリサーチ&テクノロジーズ(コンサル) 大和総研*DIR*(コンサル) NTTデータ経営研究所 日本M&Aセンター リクルート 日本IBM(SE) NTTデータ Accenture(SE) キリン 三井住友銀行(総合職) 日本生命(総合) 格付投資情報センター*R&I* 東京エレクトロン 旭化成 AGC シーメンス ソニーミュージック バンダイナムコ メタルワン 第一三共 アステラス製薬 中外製薬 日鉄興和不動産 首都高速 McCann 毎日新聞 東海テレビ 中京テレビ CBCテレビ 名古屋テレビ
【63】シグマクシス NTTドコモ KDDI 日鉄ソリューションズ 三井住友信託銀行(Gコース) 三菱UFJ信託銀行 三井住友海上(総合職) 野村證券(オープン) オリックス 第一生命(総合職) 信金中央金庫 全国銀行協会 鹿島建設 JR東日本 JR西日本 中部電力 東京メトロ 京浜急行電鉄 j&j ユニリーバ(マーケ以外) 三菱重工 日本製鉄 日立製作所 石油資源開発*JAPEX* 出光興産 小松製作所 3Mジャパン エーザイ 住友電気工業 三菱ケミカル アサヒ ADK ONE Avex ローカル局(在阪・在名除く)
=====早慶地帝勝ち=====
【62】クニエ ベイカレントコンサルティング SoftBank エムスリー DeNA Yahoo! 日本HP パナソニック 富士通 電通国際情報サービス NTT東日本 LINE ヒューレット・パッカードエンタープライズ*HPE* 商工組合中央金庫 住友生命(総合職) 明治安田生命(総合職) みずほFG(OP) SMBC日興証券(オープン) 大和証券(オープン) 野村信託銀行 AIG損害保険 JA共済 日本銀行(特定職（業務）) 日本財団 日本政策金融公庫 日本証券金融 証券保管振替機構 損保料率算出機構 日本貿易保険 三井住友カード 日揮 JFEスチール 住友化学 三井化学 花王(マーケ以外) 資生堂(マーケ以外) 東レ 信越化学 東京電力 東邦ガス 小田急電鉄 飯野海運 NEXCO中日本 大林組 大成建設 清水建設 本田技研工業 デンソー ディスコ ボッシュ 日清食品 日清製粉 明治 キッコーマン ネスレ日本 ハウス食品 長瀬産業 兼松 JFE商事 協和キリン KOSE 大塚製薬  クボタ Amazon(Operation) JSR JR東日本企画 ポニーキャニオン 日本音楽著作権協会*JASRAC* 東映 中日新聞 西日本新聞 三井不動産レジデンシャル ナイキ アディダス 損害保険ジャパン
【61】中央日本土地建物 REVAMP 博報堂コンサルティング ジャストシステム 日立コンサルティング サイバーエージェント 電通デジタル NTT西日本 日本電気*NEC* 三井住友銀行(リテール) SMBC信託 三菱UFJモルガンスタンレー証券(オープン) JCB 伊藤忠エネクス 日鉄物産 阪和興業 住友金属鉱山 竹中工務店 日産化学 豊田自動織機 日産 島津製作所  川崎重工業 ダイキンIHI 塩野義製薬 JX金属 三菱ガス化学 村田製作所 ブリヂストン 帝人 積水化学 田辺三菱 日本ロレアル(マーケ以外) 東ソー ライオン バンダイ カゴメ サッポロビール アッヴィ アドバンテスト エスティーローダ エリクソン オムロン電源開発 阪神高速 コスモエネルギー 千代田化工 近鉄GHD NSユナイテッド海運 NEXCO東日本 NEXCO西日本 九州電力 東北電力 京王電鉄 大阪メトロ 東武鉄道 西武鉄道 名古屋鉄道 京阪HD スクエアエニックス コナミデジタルエンタテインメント WOWOW 北海道新聞 河北新報 中国新聞 
【60】日本総合研究所*JRI* (IT)シンプレクス ウルシステムズ 楽天グループ 伊藤忠テクノソリューションズ*CTC* トレンドマイクロ フューチャー 日本ユニシス*BIPROGY* JSOL アフラック アサヒ飲料 グリコ ユニ・チャーム 中国電力 四国電力 三菱倉庫 DIC 三菱マテリアル TOTO いすゞ シマノ アイシン 大陽日酸 京セラ レゾナック セガサミー カプコン オリエンタルランド エプソン KIOXIA キヤノン クラレ 森永乳業 森永製菓 栗田工業 スクリーン 東芝 古河電気工業 住友重機械工業 三井金属 ヤマハ発動機 住友林業 ロート製薬 大正製薬 オリンパス 神戸製鋼 大同特殊鋼 JA全農 安川電機 ヤマハ 日清紡 UR都市機構 キングレコード 産経新聞 時事通信 新潟日報 静岡新聞 信濃毎日新聞 京都新聞 神戸新聞 山陽新聞 日本工営 建設技術研究所 パシフィックコンサルタンツ みずほ証券(オープン) 日本証券業協会 日本損害保険協会 生命保険協会
=====MARCH関関同立優秀層勝ち=====
【59】NTTデータ子会社上位(システム技術/先端技術) NTTコムウェア レコフ 日本能率協会コンサルティング*JMAC* スカイライト イグニションポイント リブコンサルティング CLIS 三菱UFJインフォメーションテクノロジー*muit*みずほリサーチ&テクノロジーズ(IT) 大和総研*DIR*(se)アバナード ベネッセ 東急エージェンシー ニッスイ ブラザー工業  ミツカン マンダム 京成電鉄 三井倉庫HD 北陸電力 沖縄電力 南海 不二製油 カルビー 日本ハム NYKバルクプロジェクト 住友商事グローバルメタルズ 岡谷鋼機 日本紙パルプ商事 稲畑産業 豊島 東京センチュリー 三井住友ファイナンス&リース 三菱HCキャピタル 横浜銀行 上田八木短資 東京短資 セントラル短資 日本郵便 東洋エンジニアリング 扶桑社 コーエーテクモ 八千代エンジニヤリング ヤマ発 トヨタ車体 カネカ 日本精工 三菱電機 デンカ 小野薬品 住友ファーマ 
【58】レイヤーズコンサルティング 山田コンサルティング 三菱UFJニコス ゆうちょ銀行 りそな銀行 松井証券 マネックス証券 かんぽ生命 あいおいニッセイ同和損保 SBI新生銀行 オリックス銀行 千葉銀行 芙蓉総合リース JA三井リース みずほリース NTTファイナンス 岩谷産業 長谷工コーポレーション タカラトミー エア・ウォーター 日本触媒 日東電工 日立建機 富士電機 大鵬薬品
【57】SCSK Sansan オービック TIS 富士フイルムビジネスイノベーション キヤノンマーケティングジャパン 興和 農中情報システム 東京海上日動システムズ 住友倉庫 JR九州 三菱地所レジデンス ソニー生命 楽天カード あおぞら銀行 アース製薬 ヴィトンギガフォトン 雪印メグミルク キユーピー ファーストリテイリング ファンケル マイクロンメモリ ルネサス 大日本印刷 電通東日本 電通西日本 読売広告社  UBE カシオ 王子HD シスメックス 日本光電 日本新薬　参天製薬 小林製薬 スバル　DMG森精機
【56】日本タタコンサルタンシーサービシズ トヨタシステムズ 日立ソリューションズ・システムズ サイボウズ マルハニチロ 都築電気 富士通Japan 大塚商会 NECソリューションイノベータ 三菱UFJトラストシステム ユニアデックス ビジネスエンジニアリング マネーフォワード セゾン情報システムズ 三井製糖 富国生命 東京スター銀行 ソニー損保 東京海上日動あんしん生命 太陽生命 大同生命 岡三証券 JR北海道 JR貨物 江ノ島電鉄 秩父鉄道 千葉都市モノレール 新京成日立造船 日立ハイテク因幡電機産業 日経広告社 朝日広告社 電通北海道・九州 日経PR オリコム AOI デジタルガレージ セプテーニ デジタルホールディングス 大広 戸田建設 五洋建設 前田建設工業 コクヨ ローム 日鉄鉱業 アシックス ユニアデックス リコー　HOYA 日粉 東京応化 ミルボン　三菱自動車 マツダ　日野自動車
【55】ニトリ パーソル レバレジーズ ニッセイ情報テクノロジー 丸紅情報システムズ 船井総研 プロレドパートナーズ プラスアルファコンサルティング オースビー ビッグツリーテクノロジー&コンサルティング アビームシステムズ ドワンゴ オービックビジネスコンサルタント 静岡銀行 中央労働金庫 三井住友海上あいおい生命保険 福岡銀行 常陽銀行 京都銀行 朝日生命 大樹生命 4大生保(営業職)  SOMPOひまわり生命 イーデザイン損保 ぐるなび 博報堂プロダクツ 凸版印刷 ダイハツ 毎日広告社 読売IS 三井住友建設 奥村組 フジタ テルモ コニカミノルタ ダイハツ TDK SHARP 三菱鉛筆 ジェイテクト リクシル　久光製薬
=====MARCH関関同立勝ち=====
"""

import re

pattern = r"==.*?=="
cleaned_data = re.sub(pattern, '', data)  # ==で挟まれた部分を削除

lines = cleaned_data.strip().split('\n')
result_dict = {}
result_dict['81'] = ['Point72', 'CapitalGroup']
for line in lines:
    match = re.match(r"\【(\d+)\】(.+)", line)  # 【80】のような部分を正規表現で抽出
    if match:
        key = match.group(1)  # 【80】の数字部分を抽出
        values = match.group(2).split()  # 【80】の後の文字列部分をリストとして抽出
        result_dict[key] = values

output_path = Path('/Users/taguchinaoki/Ranking/Data/corporation.json')
with open(output_path, mode="wt", encoding="utf-8") as f:
    json.dump(result_dict, f, ensure_ascii=False, indent=2)