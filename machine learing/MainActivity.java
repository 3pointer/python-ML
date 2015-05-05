package com.example.ec;

import java.util.ArrayList;


import java.util.List;

import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.RadioGroup.OnCheckedChangeListener;
import android.widget.TextView;
import android.view.View.OnClickListener; 

public class MainActivity extends ActionBarActivity {
    private RadioGroup group; 
    private RadioButton rb1 ; 
    private RadioButton rb2 ; 
    private Spinner spinner1;
    private Spinner spinner2;  
    private ArrayAdapter<String> adapterP;  
    private ArrayAdapter<String> adapter2M;
    private ArrayAdapter<String> adapterMethod;  
    private Button button1;
    private TextView textView1;

    private String pStr = " bit prime field";
    private String mStr = " bit binary field";
    private List<String> listP = new ArrayList<String>(); 
    private List<String> list2M = new ArrayList<String>();
    private List<String> listMethod = new ArrayList<String>(); 

    private EC_GF2m ec2m;
    private EC_GFp ecp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        group = (RadioGroup) findViewById(R.id.radioGroup1); 
        this.rb1 = (RadioButton) this.findViewById(R.id.radio0) ; 
        this.rb2 = (RadioButton) this.findViewById(R.id.radio1) ;
        spinner1 = (Spinner)this.findViewById(R.id.spinner1);
        spinner2 = (Spinner)this.findViewById(R.id.spinner2);

        for(int i = 0; i < gfp.length; i ++){
            listP.add(gfp[i] + pStr);
            list2M.add(gf2m[i] + mStr);
        }

        listMethod.add("Point Addition Operation");
        listMethod.add("Double Point  Operation");
        listMethod.add("Scalar Multiplication Operation");

        adapterP = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item, listP);  
        adapter2M = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item, list2M);  
        adapterMethod = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item, listMethod);  
        adapterP.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);    
        adapter2M.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        adapterMethod.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapterP);
        spinner2.setAdapter(adapterMethod);

        group.setOnCheckedChangeListener(new OnCheckedChangeListener() { 
            @Override 
            public void onCheckedChanged(RadioGroup group, int checkedId) { 
                // 根据ID判断选择的按钮 
                if (checkedId == R.id.radio0) { 
                    //System.out.println("1"); 
                    spinner1.setAdapter(adapterP);

                } else { 
                    //System.out.println("2"); 
                    spinner1.setAdapter(adapter2M);
                } 
            } 
        }); 


        button1 = (Button)findViewById(R.id.button1);

        button1.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                int s1number = spinner1.getSelectedItemPosition();   //获取选择Spinner1 编号 0～len-1
                //System.out.println(s1number);


                int s2number = spinner2.getSelectedItemPosition();//获取选择Spinner2编号 0～len-1
                //System.out.println(s2number);

                textView1 = (TextView)findViewById(R.id.textView1);

                ec2m = new EC_GF2m(717);

           
                EC_Point a = new EC_Point();
                a.x = "09D73616F35F4AB1407D73562C10F";
                a.y = "0A52830277958EE84D1315ED31886";
                EC_Point b = new EC_Point();
                b.x = "57CF52A0F9318000EE0BC032D756";
                b.y = "60AEE03BBCFF537A8D17401F006C";
                EC_Point ans = ec2m.dbl(a, 1);
                textView1.setText(ans.x);
            }
        });

        //     ecp = new EC_GFp(704);
        //    EC_Point ans = ecp.mul(a, "3");


        //  EC_Point ans = ec.add(a, b);
        //    textView1.setText(ans.x + ", " + ans.y);


    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }


    String[][][] strGFp =
    {
        {//112
            {
                "09487239995A5EE76B55F9C2F098",
                "a89ce5af8724c0a23e0e0ff77500"
            },
            {
                "57CF52A0F9318000EE0BC032D756",
                "60AEE03BBCFF537A8D17401F006C"
            },
            {
                "CFC1E3447FC33E5C2A7D2BF71298",
                "5BD6AC32F0A9E7AAB6AF722C3CB7"
            },
            {
                "5B2B9A62EEB59F85AC617E20A27C",
                "C0D34BE4DD15ED7C1749ECAEEEDE"
            },
            {
                "CA188CA33FDE3CE02A83F197547C",
                "AB5C59CB715E2DDC3E51AD252A5F"
            },
            {
                "12816A28C5FA3B44DAEA1FD67E50",
                "2E4A2B63845A4C632BF992CBBED"
            },
            {
                "B0E10FC47C14FC35B2CF498CC15F",
                "C9F73C24918F44444D04E77FE46A"
            },
            {
                "17FC3DAAEAE82364456158BD6E9B",
                "5931D7B7B7D5B4BB2DE33A88746F"
            }

        }, 
        {//128
            {
                "161FF7528B899B2D0C28607CA52C5B86",
                "cf5ac8395bafeb13c02da292dded7a83"

            },
            {
                "8151A0C6B92171DB199DB84BE753A97E",
                "3D853559455CAAE838395A9275B7E95"
            },
            {
                "AD632F542942F23AA423B628A304B3B",
                "7AA67EE421C4E78851E4B4679BCDC41F"
            },
            {
                "47487E914AAE409DECB6495FBDD2647F",
                "4E67A67404C56AE34783239F70A198D3"
            },
            {
                "E147E5D422BB217E35493632B5D3E53F",
                "85563E321E03170A929451838E740757"
            },
            {
                "624BCC28BF7670B76E6D3B61D2247FEF",
                "92C2A43957B12F98BB52F92BA856B06"
            },
            {
                "70416BB15D70A474DE75BD2340D215F2",
                "E4361E1EEFB356C57CEE5C841A4687BE"
            },
            {
                "EE6682773350C39D5DFAE6717FDB254",
                "3209FFF0799AA1915D17D982991E966A"
            }
        },
        {//192
            {
                "188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012",
                "07192b95ffc8da78631011ed6b24cdd573f977a11e794811"
            },
            {
                "DAFEBF5828783F2AD35534631588A3F629A70FB16982A888",
                "DD6BDA0D993DA0FA46B27BBC141B868F59331AFA5C7E93AB"
            },
            {
                "76E32A2557599E6EDCD283201FB2B9AADFD0D359CBB263DA",
                "782C37E372BA4520AA62E0FED121D49EF3B543660CFD05FD"
            },
            {
                "35433907297CC378B0015703374729D7A4FE46647084E4BA",
                "A2649984F2135C301EA3ACB0776CD4F125389B311DB3BE32"
            },
            {
                "10BB8E9840049B183E078D9C300E1605590118EBDD7FF590",
                "31361008476F917BADC9F836E62762BE312B72543CCEAEA1"
            },
            {
                "A37ABC6C431F9AC398BF5BD1AA6678320ACE8ECB93D23F2A",
                "851B3CAEC99908DBFED7040A1BBDA90E081F7C5710BC68F0"
            },
            {
                "8DA75A1F75DDCD7660F923243060EDCE5DE37F007011FCFD",
                "57CB5FCF6860B35418240DB8FDB3C01DD4B702F96409FFB5"
            },
            {
                "2FA1F92D1ECCE92014771993CC14899D4B5977883397EDDE",
                "A338AFDEF78B7214273B8B5978EF733FF2DD8A8E9738F6C0"
            }
        },
        {//224
            {
                "B70E0CBD6BB4BF7F321390B94A03C1D356C21122343280D6115C1D21",
                "bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34"
            },
            {	
                "706A46DC76DCB76798E60E6D89474788D16DC18032D268FD1A704FA6",
                "1C2B76A7BC25E7702A704FA986892849FCA629487ACF3709D2E4E8BB"
            },
            {
                "DF1B1D66A551D0D31EFF822558B9D2CC75C2180279FE0D08FD896D04",
                "A3F7F03CADD0BE444C0AA56830130DDF77D317344E1AF3591981A925"
            },
            {
                "AE99FEEBB5D26945B54892092A8AEE02912930FA41CD114E40447301",
                "482580A0EC5BC47E88BC8C378632CD196CB3FA058A7114EB03054C9"
            },
            {
                "31C49AE75BCE7807CDFF22055D94EE9021FEDBB5AB51C57526F011AA",
                "27E8BFF1745635EC5BA0C9F1C2EDE15414C6507D29FFE37E790A079B"
            },
            {
                "1F2483F82572251FCA975FEA40DB821DF8AD82A3C002EE6C57112408",
                "89FAF0CCB750D99B553C574FAD7ECFB0438586EB3952AF5B4B153C7E"
            },
            {
                "DB2F6BE630E246A5CF7D99B85194B123D487E2D466B94B24A03C3E28",
                "F3A30085497F2F611EE2517B163EF8C53B715D18BB4E4808D02B963"
            },
            {
                "858E6F9CC6C12C31F5DF124AA77767B05C8BC021BD683D2B55571550",
                "46DCD3EA5C43898C5C5FC4FDAC7DB39C2F02EBEE4E3541D1E78047A"
            },
        },


        {//239

            {
                "0FFA963CDCA8816CCC33B8642BEDF905C3D358573D3F27FBBD3B3CB9AAAF",
                "7debe8e4e90a5dae6e4054ca530ba04654b36818ce226b39fccb7b02f1ae"
            },
            {
                "108D8BA279D0574D852F50E02A7C8800FE1436417B9C0791C9BAAF281C78",
                "6A9F83241106BD86431843F61291C8C5AA3580E0FA3580C565EDC2C432C5"
            },
            {
                "22DBC8D0EC84C7EC9706FE55F226E24F4152950E4BF28A2EC2E908186360",
                "141AB1DC0DE87873AA10719ED8ED1BF00A1680FA3C41879AACAB9E85CDE3"
            },
            {
                "6EC016F7CE5BA5F5660CF277A40329D3A32808060904551E67B5E33EC481",
                "5212DF000F3890A003ABBDDF122B7D39BEDF40BEE36AB861485E9495C38B"
            },
            {
                "FD7A27B9ABB671BCD01CB0072E24B9D3EBA9022019F300A487ECF569668",
                "79F11A619ADF1D847FAF7789F27CB2E4398A7935D134B02C14EAC556FF4B"
            },
            {
                "68DA2CEBE1D0EA92B54F542FDA170877F9A4FA749C7F4003F79E6E8A5C0D",
                "1CD0F6E138BC4F62F5CC29753D9F06FD46F5BE1B1504AB37595F8C5964F3"
            },
            {
                "78221FD4D8D0EF7C53ABD1CE2A66F2587F1FFBC2305ACE68BBAF030F5A02",
                "73E72F45165E76A8F767C7851FCF0BDB8296BEBD87C1761816BC8D06EADD"
            },
            {
                "15D1922054CD402848296836348C69F7A7D7A33284513487087BDC35F00D",
                "19E96149EA54EB9B6D02036E350BA4EF2F858BE78456DB1D9549D49A148"
            },
        },	

        {//256
            {
                "6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296",
                "4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5"
            },				
            {
                "7CF27B188D034F7E8A52380304B51AC3C08969E277F21B35A60B48FC47669978",
                "7775510DB8ED040293D9AC69F7430DBBA7DADE63CE982299E04B79D227873D1"
            },
            {
                "5ECBE4D1A6330A44C8F7EF951D4BF165E6C6B721EFADA985FB41661BC6E7FD6C",
                "8734640C4998FF7E374B06CE1A64A2ECD82AB036384FB83D9A79B127A27D5032"
            },
            {
                "E2534A3532D08FBBA02DDE659EE62BD0031FE2DB785596EF509302446B030852",
                "E0F1575A4C633CC719DFEE5FDA862D764EFC96C3F30EE0055C42C23F184ED8C6"
            },
            {
                "51590B7A515140D2D784C85608668FDFEF8C82FD1F5BE52421554A0DC3D033ED",
                "E0C17DA8904A727D8AE1BF36BF8A79260D012F00D4D80888D1D0BB44FDA16DA4"
            },
            {
                "B01A172A76A4602C92D3242CB897DDE3024C740DEBB215B4C6B0AAE93C2291A9",
                "E85C10743237DAD56FEC0E2DFBA703791C00F7701C7E16BDFD7C48538FC77FE2"
            },
            {
                "8E533B6FA0BF7B4625BB30667C01FB607EF9F8B8A80FEF5B300628703187B2A3",
                "73EB1DBDE03318366D069F83A6F5900053C73633CB041B21C55E1A86C1F400B4"
            },
            {
                "62D9779DBEE9B0534042742D3AB54CADC1D238980FCE97DBB4DD9DC1DB6FB393",
                "AD5ACCBD91E9D8244FF15D771167CEE0A2ED51F6BBE76A78DA540A6A0F09957E"
            },

        },

        {//384
            {
                "AA87CA22BE8B05378EB1C71EF320AD746E1D3B628BA79B9859F741E082542A385502F25DBF55296C3A545E3872760AB7",
                "3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f"
            },

            {
                "8D999057BA3D2D969260045C55B97F089025959A6F434D651D207D19FB96E9E4FE0E86EBE0E64F85B96A9C75295DF61",
                "8E80F1FA5B1B3CEDB7BFE8DFFD6DBA74B275D875BC6CC43E904E505F256AB4255FFD43E94D39E22D61501E700A940E80"
            },
            {
                "77A41D4606FFA1464793C7E5FDC7D98CB9D3910202DCD06BEA4F240D3566DA6B408BBAE5026580D02D7E5C70500C831",
                "C995F7CA0B0C42837D0BBE9602A9FC998520B41C85115AA5F7684C0EDC111EACC24ABD6BE4B5D298B65F28600A2F1DF1"
            },
            {
                "138251CD52AC9298C1C8AAD977321DEB97E709BD0B4CA0ACA55DC8AD51DCFC9D1589A1597E3A5120E1EFD631C63E1835",
                "CACAE29869A62E1631E8A28181AB56616DC45D918ABC09F3AB0E63CF792AA4DCED7387BE37BBA569549F1C02B270ED67"
            },
            {
                "11DE24A2C251C777573CAC5EA025E467F208E51DBFF98FC54F6661CBE56583B037882F4A1CA297E60ABCDBC3836D84BC",
                "8FA696C77440F92D0F5837E90A00E7C5284B447754D5DEE88C986533B6901AEB3177686D0AE8FB33184414ABE6C1713A"
            },
            {
                "627BE1ACD064D2B2226FE0D26F2D15D3C33EBCBB7F0F5DA51CBD41F26257383021317D7202FF30E50937F0854E35C5DF",
                "9766A4CB3F8B1C21BE6DDA6C14F1575B2C95352644F774C99864F613715441604C45B8D84E165311733A408D3F0F934"
            },
            {
                "283C1D7365CE4788F29F8EBF234EDFFEAD6FE997FBEA5FFA2D58CC9DFA7B1C508B05526F55B9EBB2040F05B48FB6D0E1",
                "9475C99061E41B88BA52EFDB8C1690471A61D867ED799729D9C92CD01DBD225630D84EDE32A78F9E64664CDAC512EF8C"
            },
            {
                "1692778EA596E0BE75114297A6FA383445BF227FBE58190A900C3C73256F11FB5A3258D6F403D5ECE6E9B269D822C87D",
                "DCD2365700D4106A835388BA3DB8FD0E22554ADC6D521CD4BD1C30C2EC0EEC196BADE1E9CDD1708D6F6ABFA4022B0AD2"
            }
            }
    };

    String[][][] strGF2m =
    {
        {//21NID_sect113r1,

            {
                "009D73616F35F4AB1407D73562C10F",
                "00A52830277958EE84D1315ED31886"
            },
            { 
                "1E705FE7C22E98D36466640BA4E11",
                "19DD2A2DC4551FEC6C5417AAEA268"
            },
            {  
                "1BEFCA336EA60C4E294D6B55F0C8F",
                "495EFEB589C3DA382CFCE77CB298"
            },
            {
                "1647BFE998DA435E059BEF9BBF47",
                "1D1E6C95F913E305BEE01E70970AA"
            },
            {
                "10D3ED70A6B3000C0475DE34A3E19",
                "1CDF9B901EE9879878FE081C37E2C"
            },
            {
                "12343B015BA5AE9AB7AE8910B1D7",
                "78FF4678F64EC5905DA3CA832F0E"
            },
            {
                "5627DF39C0AF87290D4D4252EF99",
                "D4A43511BA4544F74FAD7AD235D3"
            },
            {
                "496EE72C68DF864F03D9AABC6861",
                "473F92EEB3AC0023075261A9A111"
            },

        },
        {//22NID_sect163r1,

            {
                "369979697AB43897789566789567F787A7876A654",
                "435EDB42EFAFB2989D51FEFCE3C80988F41FF883"
            },
            {
                "4E1456FFEAD56A68862E3006A87BCF6D6FC3672B4",
                "223F5DD8AB164D4E51D903623764F48A787E528A8"
            },

            {
                "48A0A8A89D53DFB023EA98CEE93381C6715AA87D1",
                "6BE5460DA1AD9AC2EFF25554DDB5FE237BAE5D412"
            },
            {
                "6580F74EE239912537F7C8BF2C2D9320D448F0057",
                "7E641D37C09C6B64909DAC22A1627D63C428DCCC9"
            },
            {
                "7D0399F55130A0C875A7C11A10DC8DAD9E0CBE1F5",
                "7CB333BE33C0D15FDC14070E84EB7ED3523F92B89"
            },
            {
                "3626E383192FFD59FDF4FF9D76E9772FDECC2CBFA",
                "3C7612920DCE1DA8501CA2D720CB1B4660EE607FB"
            },
            {
                "62F810DD8AC3AD45019970812DC3C1C9FCF61EDB8",
                "4DFB2C762C5066B26DCEE6147271DF5561E319764"
            },
            {
                "4C0D68075E57763C347B5E3B8AE12FB849AA8A81",
                "352E153FB86E32CAAD4B5E4275C22257385C017A3"
            }
        },
        {//23NID_sect193r1,
            {
                "01F481BC5F0FF84A74AD6CDF6FDEF4BF6179625372D8C0C5E1",
                "0025E399F2903712CCF3EA9E3A1AD17FB0B3201B6AF7CE1B05"
            },			
            {
                "7F9311AAB549CF950746C04B5B552D2ECA197C1413061CE7",
                "2FEFAFD1872508BDE92F12B695543B76A1C16B348597B1E4"
            },
            {
                "17A1644D5A5EE5F7D38FFC105659D115D0FCB037EC5EBC8E1",
                "1EA116683A89575D97F3BE5C717A4924E4C9B0C5209A3B990"
            },
            {
                "178B0EE8683731B05DFF6D6A048A94C1AE9F574E608A2FC49",
                "85ABFB152A3E2FB6E1856191F74F474D24F5C5D1FC170105"
            },
            {
                "14094FF19981F3D6A4BFB07B090F2E36B453D3B960CD0238D",
                "1077495CDE51C4F004974D35D3DB97699C87A20C98909ADB7"
            },
            {
                "1F65564E6FE586A26203F54AECC8900E4576EAF8BBE57A8A7",
                "FA67DF3D4FDF14508BD7387FB61758B3B6D1003F4572DFF8"
            },
            {
                "14042EE9EBF28C910DD6FACFF9DCEB7A60C2E93BCBC3A1C6B",
                "A2062DEC936E4F7E1DD0558E1F64D6FABFD8F6AA111CEF4D"
            },
            {
                "3F8711747A22C7DEF455E37862355004E13E1318052EFA5B",
                "5341A4718472C3CE38F8F96427EBECA5AC4F2B415D0DCA37"
            }
        },
        {//24NID_sect233r1,
            {
                "00FAC9DFCBAC8313BB2139F1BB755FEF65BC391F8B36F8F8EB7371FD558B",
                "01006A08A41903350678E58528BEBF8A0BEFF867A7CA36716F7E01F81052"
            },
            {
                "845FD61638BAC7D9E109A67A1F7047DC0FD9A5488A8468364BDC592AAD",
                "1B1420774ABBA2587C83900984765A8A85D776325FC39CC7823D734660"
            },	
            {
                "80F50A330911BD753A76364595B9F0158C4D02A85CC0E3FB6EA0AEF9FF",
                "17A49033F12EB52675E98E6432CC27104BD5C42BCBE3DAF76901C9B8743"
            },
            {
                "63A1BAAAC9B4861CB6AAC5B38889A57A9629C7B04E7825CEB3FB4428A8",
                "132A03FAE14E34053D6CCEACC117BFF8EFAF5F008D32AB626CBF9012209"
            },
            {
                "194ED0CA60C85E59E7C4B69F30C6304A9F485F45032B871C4A23FFEC8C1",
                "A52F9459C2FAB39C214061E272E1E115E1E01A98E4F09CD5A85D2698C6"
            },
            {
                "2EEDA3493C16230768A46AB073F6A5433FE5617BD4AFE57CC825D27276",
                "C0C4C68F81C3BD0202A4EC28FFD13E208F4271701CD96887A5806028FC"
            },
            {
                "1F7D14C8236367ED87EB63873C754BD8B7EC794D966B02E26C932B29F9C",
                "8F7C01DF764B179486CFC7B5658C1829BAF50AF0DD42E822556F72CEEA"
            },
            {
                "1113FA420BBE57886A2FC590E99666864D0889BAE81DFA59EF439DD177",
                "FBBEE98D579FEFEA0E811284146297E14321159B46700CDF49FFD07354"
            }
        },
        {//25NID_sect239k1,
            {
                "29A0B6A887A983E9730988A68727A8B2D126C44CC2CC7B2A6555193035DC",
                "76310804F12E549BDB011C103089E73510ACB275FC312A5DC6B76553F0CA"
            },

            {
                "38B8E2A7BD7FB488C092DFF4C83A6AB8AC294CF62C28C860D506BBC33609",
                "78B72287286F99B2C72982F0D72BF12DD59AE9474EA14DE6703795A558F9"
            },
            {
                "2C0BD50B5635F213163FF631773753CE2D314D7CDF0C9889EE1AAC81F841",
                "569F9DA91FBD99A827F0CDC81FCD5EE03FF1C45DAF85F0646E00AD3EE65C"
            },
            {
                "6868FBC7EC18EA9B3B5E890937AE2879B20A297D285F5FE06013A2813BB9",
                "1D72E57E478CD9446D3A6FBA9494A9FC83EC04BEABC0B2BF2E0561F05352"
            },
            {
                "282C8215E0B6434AFDE5590BC9E3B5AF3DB69AE633C0004EC29385615828",
                "5C12BBD2F7284E12866E3A869331FA8696C385892095CFAAD83DE2A130F"
            },
            {
                "DD24420880A56BF6A6F336ED4F63B98A586FAF0D58817482234750AA22B",
                "5345F440F2574AD244FFA308263515C2E63AC84E2AC9C7E4121FEE9F411F"
            },
            {
                "272B272B4ABD5A8127DFB9147DF00968D4B77F9DE97A789A95B35E6B70A7",
                "5706B75ADD13151D6B12D563899426A60E5B0700378E1E6CDC4517A75C46"
            },
            {
                "22F94BBD4B5586F9BF14E06BE38298FB294A3F7B9CB218BC278F91F06B9A",
                "6FD27D58715F013F251051B423BAE9517D4E803C9870B0E9CC3AF63B1D0E"
            }
        },
        {//26NID_sect283r1
            {
                "0503213F78CA44883F1A3B8162F188E553CD265F23C1567A16876913B0C2AC2458492836",
                "01CCDA380F1C9E318D90F95D07E5426FE87E45C0E8184698E45962364E34116177DD2259"
            },  


            {
                "30AE969B9792D44BFDAE086DC6FA1039E52A459A545E78B57A1C9D749C1DC6FAEAF80CF",
                "59D726AA1B70C5E9FFA46D6A1F912B31480BC3D8E0CAB1666497F16B970256427B2FC02"
            },
            {
                "15DCCC30A8B1F5146412D51FEC337741090321408AAC521391AD36C5912E280124FE3B5",
                "53FC9BED137312952AD97F6A98C4C7AC1B421635FBAFE28898E9213D979D5B4D279F192"
            },
            {
                "3949AFAEDDDE457A6B7F17129776A4EA5C5C671594A553C5F1DFC1C2C6C5D36CC6F7B91",
                "286EE1883F14F990BD23310F6212E0CB2578DE1DC43C6B52729D57A5FE072317C1AFB8E"
            },
            {
                "7879D57C3BD1A1A0F42683ACFC15E85022BAD17D02FF0AB922348199EC2E8F524A2B90D",
                "745950630769FB467205FC95653FBB4FC2487E22EE749AEB9F1B0ACB848691ABD2D7DF8"
            },
            {
                "24C13AB84AD4DAA481ECE8B2C5264EB0E14E66FB919EEEE7CDF66B00A99DD7D749CD1EC",
                "66A9E12C943F9EDD1354B283F88161927C9FA53C38183C8004E8DD69BA1DADE5DA6D837"
            },
            {
                "16316C84BE2D17E2A4B035B4DFEE6EB538535B215EDF4C189B5EB2B4C72DD4D641474BE",
                "2119B23FE3B6B8A8F32928F855B4028A3FAA8F6A81488B2B177F000F81CEFD51FA1096A"
            },
            {
                "709EA1B81C8627D967299BD1A5A4120645CE3E3104F137D55BA5BD08C89488DBA3A7635",
                "80F27925956E3D468C49305268509E2BAAA30CCB1FC63DB8D19396E5FFE7F3A646FDDC"
            }
        },
        {//27NID_sect409r1,
            {
                "015D4860D088DDB3496B0C6064756260441CDE4AF1771D4DB01FFE5B34E59703DC255A868A1180515603AEAB60794E54BB7996A7",
                "0061B1CFAB6BE5F32BBFA78324ED106A7636B9C5A7BD198D0158AA4F5488D08F38514F1FDF4B4F40D2181B3681C364BA0273C706"
            },

            {
                "1EB8E16DA624068B00C1E75B0C176E7FAD804795C9CCDA32EE3F5947F71F86638D81EB398C8E1CE4024249CDD45D1AA3876171",
                "105BEA9950494E2BA93939D280CCD110E82F700722DC06967E6A2ABF2876D267A60628FC0C01560D62DE46C3EB733C06A8F14B2"
            },
            {
                "D5F0E8B27D12D7A9DCEA13A5CFB9DEE62D63376E31F7666BA2AC2BF314B91420749EF549A17E5DC6815A7B044FF458C40C415", 
                "1DB5B78D491E45CC58E9E44BD7E42537597B9ABA85E2E3589F02D466ED31B816235F6D22679690002FCEF2B5390F0DE885E90BE",
            },
            {
                "17F83AD07F6DCC7C2064E74FEE189D88BAE4437B159A90E449FC23AB79D43C16D1B95E9B3BB35E32450D02419ABA40B18318C17",
                "9088328FB9A24F7D9ED1BAE65DFC4CD7558BE314A925D7046A11CD8E196D878169352C50DFF0DEAD68DD369E1BEF916EEFA36C"
            },
            {
                "4654FED823C1DD4869E734045CBE81C2B2490ECF7FDD4A5282DEB135B35340B9E607BB43552C3982B03ACE3DA8E257964A66D",
                "A2900F935DF4B06371EFC32572C40C3A85AABDFF94B7050E5C5223AD6A56413C2D5CE9C95832B1B68F59BA29FF878F571DAEE9"
            },
            {
                "3A39CD20D0B1865197CE0C3B051C64E19631A9F4E13230E15B1CAB68B3060E26ED6AA0AA8D495C2413DD2EE60BDBE035A0CF7D",
                "12488FE8BB58879DAE5F3F798EF2795BAF09A969AE778912ED228FD7D8830D1CE0542782937AAA34F593B2E5A7120A74F705D7B"
            },
            {
                "1374FDE9C26F1DA72FE4AC3BAAE876EB15B248A9307F87C5359BFAE5CF1893AAF34B22B46903F022759FF34E6DE38A979768E5F",
                "187476EE32346BD72D2C3172B1C7F395B101EFB396E4BBCC3600251B18DAAE556F69929F52003FBC7117A42C03548F6E1CF4208"
            },
            {
                "1BD32BC1E109875EB9E6842F4E41CE5164E7CB3813FA4EC9D8817282178BA7931B1909513DAE3FC72054BCD951BF7E0AC340CC7",
                "D3AA451E8CC0DAEED8CFFB6DD5A9E734017754658F4F8B59D123DC038172770A9E51106A05CD32EC0D562600A870F104104324"
            }
        }	
    };

    String[] gfp = {
        "112", "128", "192", "224", "239", "256", "384" 	
    };

    String[] gf2m = {
        "113", "163", "193", "232", "239", "283", "409" 	
    };

    String[] scalar = {
        "3", "7", "18", "35", "76", "159", "321", "639", "1273", "2540"	
    };

}
