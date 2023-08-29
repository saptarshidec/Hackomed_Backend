# mcv=input("Enter the MCV value in fl")
# mch=input("Enter the MCH value in pg")
# mchc=input("Enter the MCHC value in g/l")
# rdw=input("Enter the RDW value as standard deviation in fl")
# rdw=input("Enter the RDW value as coefficient of variation in %")

def calc(mcv,mch,mchc,rdw):
    mcv_prediction=""
    mch_prediction=""
    mchc_prediction=""
    rdw_prediction=""

    # Haemoglobin <13.5 -> Anaemia
    # Haemoglobin 13.5-17.5 -> Normal
    # Haemoglobin >17.5 -> High

    # Reticulocyte count <0.5 Low
    # Reticulocyte count >2.5 High

    # Iron Deficiency Anaemia -> Microcytic, Hypochromic, RDW High

    # Haemoglobin 11
    # MCV 72
    # MCH 23
    # RDW 19
    # MCHC 31.9
    # Reticulocyte count 3.1

    if(mcv<82):
        mcv_prediction="Microcytic anaemia"
    elif(mcv>100):
        mcv_prediction="Macrocytic anaemia"
    else:
        mcv_prediction="Normocytic anaemia"

    if(mch<27):
        mch_prediction="Hypochromic anaemia"
    elif(mch>32):
        mch_prediction="Hyperchromic anaemia"
    else:
        mch_prediction="Normochromic anaemia"

    if(mchc<33):
        mchc_prediction="Low MCHC"
    elif(mch>37):
        # mchc_prediction="MCHC above normal, may be Hereditary Spherocytosis"
        mchc_prediction="MCHC above normal"
    else:
        # mchc_prediction="MCHC value normal, may be Megaloblastic Anaemia"
        mchc_prediction="MCHC value normal"

    # if(rdw<39):
    #     print("Low RDW")
    # if(rdw>46):
    #     print("RDW above normal, may be Iron Deficiency Anaemia")
    # else:
    #     print("RDW value normal, may be Thalassaemia")

    if(rdw<11.5):
        rdw_prediction="Low RDW"
    elif(rdw>14.5):
        # rdw_prediction="RDW above normal, may be Iron Deficiency Anaemia"
        rdw_prediction="RDW above normal"
    else:
        # rdw_prediction="RDW value normal, may be Thalassaemia"
        rdw_prediction="RDW value normal"


    return mcv_prediction,mch_prediction,mchc_prediction,rdw_prediction