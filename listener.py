import webbrowser
from time import sleep

import requests


COOKIES = 'pe=p1; aat1=on; acctdel_v1=on; adh_new_ps=on; adh_ps_pickup=on; adh_ps_refill=on; buynow=off; sab_displayads=on; dashboard_v1=off; db-show-allrx=on; disable-app-dynamics=on; disable-sac=on; dpp_cdc=off; dpp_drug_dir=off; dpp_sft=off; getcust_elastic=on; echomeln6=off-p0; enable_imz=on; enable_imz_cvd=on; enable_imz_reschedule_instore=on; enable_imz_reschedule_clinic=off; flipp2=on; gbi_cvs_coupons=true; ice-phr-offer=off; v3redirecton=false; mc_cloud_service=on; mc_hl7=on; mc_home_new=off2-p0; mc_ui_ssr=off-p2; mc_videovisit=on; memberlite=on; pauth_v1=on; pivotal_forgot_password=off-p0; pivotal_sso=off-p0; pbmplaceorder=off; pbmrxhistory=on; ps=on; refill_chkbox_remove=off-p0; rxdanshownba=off; rxdfixie=on; rxd_bnr=on; rxd_dot_bnr=on; rxdpromo=on; rxduan=on; rxlite=on; rxlitelob=off; rxm=on; rxm_phone_dob=off-p1; rxm_demo_hide_LN=off; rxm_phdob_hide_LN=on; rxm_rx_challenge=off; s2c_akamaidigitizecoupon=on; s2c_beautyclub=off-p0; s2c_digitizecoupon=on; s2c_dmenrollment=off-p0; s2c_herotimer=off-p0; s2c_newcard=off-p0; s2c_papercoupon=on; s2c_persistEcCookie=on; s2c_rewardstrackerbctile=on; s2c_rewardstrackerbctenpercent=on; s2c_rewardstrackerqebtile=on; s2c_smsenrollment=on; s2cHero_lean6=on; sft_mfr_new=on; sftg=on; show_exception_status=on; v2-dash-redirection=on; ak_bmsc=278E548D13015E107B1864057A872D4217DB24854D3E000088D85760992BC65C~plOmkTxv9f49dqIqFvifGJCOpr/yLwTEPmUnQUwcDS8Br/yAWS4E0dU1R6ZvUtsdwDqHGGVUg2snjZqiGUqHZsQ046b7bqvqfZjE9QQVlQZ7Mhc5QLUoLvt3Jz2+ES0ybwWgWhI1MwFMj1sw+aG6XELmC3pm7xKRkV6GWNe1i76GAgid/oWWW94bFLj5k9LQNhXgDFYwrIWqoRuJWLVEKCMNriCogkvXaXYJFgXeXbJpw=; bm_sz=2E661B343F505D1C697D26DF3F342E81~YAAQhSTbF/ZJ4zx4AQAAytMlVwuyPldMKMZ6bok8HM3oLhd+lYgV6vReJnZkykq1Rde+jfoeX4BybZAxzNVkN7EH4QkMvITRk9GQrs0oI7XPNHdNUvli4h++4cn1J59TqKL3TTrb/NTwIGrZSUsxt6BzNwkX73ysAeIS51M1uNBhzq+d97Qs3ujI901d; mt.v=2.745406475.1616369800542; _group1=quantum; gbi_sessionId=ckmjsugj200003h8nnqwcpndc; gbi_visitorId=ckmjsugj200013h8ns9etow3l; AMCVS_06660D1556E030D17F000101@AdobeOrg=1; mt.sc={"i":1616369801078,"d":[]}; _abck=16B1BC6D820C462B3D5C77E9D2FA9664~0~YAAQhSTbFwVK4zx4AQAAYNklVwVspA7nZTaCKGoXSYanOOX9O7duzDd6dhRHnQjSKvliocdOhUsoN9qhCTch2X1nNJ4/AcVkykrxCi+mLLA87B1tM6Rrc5guGORvzhFReEj+nh2i1mDSKN6pDjof3jCAxP1SNxhqzsIk34sX2zXdUpz2xyiTDOTRIJxvSkwcFde69JUSczM9/ZUAED2mqA5w49h5sG+/qcAH/3KjYcxNCdyAQeC7LtpZbM6ksqM1QvGs/p733N/4p7ag2t4mnGLke6lBSKr0z9DcvEpnN5SnKuzSDhuWRhgg4CqXJ0FHQzpFVj4+p51lTZaBRUoFLmBx55Yw5sR0Os8tGdo2PHdrVHMgzsWfMlZZNxxnVUoZ6X0bq+pKBvsUisWHNb3+mj7lHJmU~-1~||-1||~-1; _gcl_au=1.1.490573097.1616369802; _4c_mc_=fd28fbf2-5265-4bc6-9af9-45a6c73f57f4; s_cc=true; QuantumMetricSessionID=f930f1ac325c33fc5a09a4bcca6b6c39; QuantumMetricUserID=629186a37bf9cd4d9b14540d831567c4; QuantumMetricSessionLink=https://cvs.quantummetric.com/#/users/search?autoreplay=true&qmsessioncookie=f930f1ac325c33fc5a09a4bcca6b6c39&ts=1616326603-1616413003; akavpau_vp_www_cvs_com_minuteclinic_covid19=1616370223~id=1bf5160bf088167c47cbce04139e3058; DG_IID=9E427292-90E3-32CF-B4AC-8DEBBE1F7062; DG_UID=82B7501F-F9D5-33DE-B881-6051DA4768F5; DG_ZID=87A0D666-0F29-30D8-8FF0-07964A9820F0; DG_ZUID=C4DDEB95-1FBD-3AEA-9ACB-BE436935B5BF; DG_HID=EBAF00AB-033E-3C28-8750-727F1F4AE959; DG_SID=163.116.133.117:c+6rFIzzA0sn8BK9xRhU8sD6iFUrAXixrFj5ucRMS/4; mt.cem=210103-v2-Homepage-Order - 210103-v2-Homepage-Order,experiment | 210210-MC-B2C-COVID - 210210-MC-Testing-VaxAlert,experiment | 210216-MCcom-Header-Banner - A-Homepage-other-locations; mt.mbsh={"fs":1616369801985,"sf":1,"lf":1616369805088}; AMCV_06660D1556E030D17F000101@AdobeOrg=-330454231|MCIDTS|18708|MCMID|72880648688561941713982977851320123920|MCAAMLH-1616974625|7|MCAAMB-1616974625|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1616377025s|NONE|MCAID|NONE|vVersion|3.1.2; mp_cvs_mixpanel={"distinct_id": "174e9bc076e2a-0dffeab3ce037c-31697304-1ea000-174e9bc076fe03","bc_persist_updated": 1616369801318}; gpv_p10=www.cvs.com/immunizations/covid-19-vaccine; affinity="69630c111b9d3342"; CVPF=3y7T2AMXC71G5Z8Pg6bbNgttCiEsx2uSmL4WOTuIhF8skYmPXU79Xdg; akavpau_www_cvs_com_general=1616370579~id=18ead1f2c042b1d713ae376ccc7a2e26; bm_sv=4144EB738A86B38577780D027C813F2F~KSzOlhuUTNVLa4sGOi4SFUwomEKcdUqcLDHtr/Ao5bk5G96mOpSzYDEMiX06H6EhfGHP8upltFHEXqUnb6p+9IHiKDNqy+BlrSksZI3YA1/EwhyNIMXml6eInoQ0IaUEgXY7fe5BjxdMwDaKdxKnmw==; gpv_e5=cvs|dweb|immunizations|covid-19-vaccine|promo: covid-19 vaccines in michigan modal; RT="z=1&dm=cvs.com&si=f99a6fc9-ec4f-46ca-8f03-c389783dc73e&ss=kmjsufnk&sl=7&tt=bp4&bcn=//17c8edc9.akstat.io/&ld=7sib&nu=ifz4dlr5&cl=8rme"; qmexp=1616372008921; s_sq=[[B]]; utag_main=v_id:01785725d6180002e161494b204503079001407100b7e$_sn:1$_ss:0$_pn:6;exp-session$_st:1616372009100$ses_id:1616369800728;exp-session$vapi_domain:cvs.com'
VICTORY_URL = 'https://www.youtube.com/watch?v=eBShN8qT4lk'
ELIGIBILITY_URL = 'https://www.cvs.com/vaccine/intake/store/cvd-schedule.html?icid=coronavirus-lp-vaccine-sd-statetool'
SLEEP_SECONDS = 10


def listen():
    availability_url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.json'
    # or this one: https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    response = requests.get(
        availability_url,
        headers=headers,
        verify=False
    )
    if response.status_code != 200:
        return

    michigan_content = response.json()['responsePayloadData']['data']['NY']
    detroit_content = {}
    for zone in michigan_content:
        if zone['city'].lower() == 'detroit':
        # if zone['city'].lower() == 'binghamton':
            detroit_content = zone
            break

    if not detroit_content:
        return False

    if detroit_content['status'].lower() == 'available':
        return True

    return False


is_victory = False
counter = 0
while not is_victory:
    sleep(SLEEP_SECONDS)
    counter += 1
    is_victory = listen()

print('Huzzah!')
webbrowser.open(ELIGIBILITY_URL)
webbrowser.open(VICTORY_URL)
print(f'That took {counter} attempts')
