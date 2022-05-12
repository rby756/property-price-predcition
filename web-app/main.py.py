from unicodedata import name
from flask import Flask, render_template,request
import numpy as np
import pickle

app = Flask(__name__)
model=pickle.load(open('property.pkl','rb'))


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
	if request.method=='POST':
		YearBuilt=request.form['YearBuilt']
		YearRemodAdd=request.form['YearRemodAdd']
		BsmtFullBath=request.form['BsmtFullBath']
		KitchenAbvGr=request.form['KitchenAbvGr']
		Fireplaces=request.form['Fireplaces']
		GarageCars=request.form['GarageCars']
		Total_SF=request.form['Total_SF']
		OverallQual=request.form['OverallQual']
		OverallCond=request.form['OverallCond']
		Dwell_Type=request.form['Dwell_Type']
		Dwell_Type_30=0
		Dwell_Type_40=0
		Dwell_Type_45=0
		Dwell_Type_50=0
		Dwell_Type_60=0
		Dwell_Type_70=0
		Dwell_Type_75=0
		Dwell_Type_80=0
		Dwell_Type_85=0
		Dwell_Type_90=0
		Dwell_Type_120=0
		Dwell_Type_160=0
		Dwell_Type_180=0
		Dwell_Type_190=0
		if Dwell_Type==1:
			Dwell_Type_30==1
		if Dwell_Type==2:
			Dwell_Type_40==1
		if Dwell_Type==3:
			Dwell_Type_45==1
		if Dwell_Type==4:
			Dwell_Type_50==1
		if Dwell_Type==5:
			Dwell_Type_60==1
		if Dwell_Type==6:
			Dwell_Type_70==1
		if Dwell_Type==7:
			Dwell_Type_75==1
		if Dwell_Type==8:
			Dwell_Type_80==1
		if Dwell_Type==9:
			Dwell_Type_85==1
		if Dwell_Type==10:
			Dwell_Type_90==1
		if Dwell_Type==11:
			Dwell_Type_120==1
		if Dwell_Type==12:
			Dwell_Type_160==1
		if Dwell_Type==13:
			Dwell_Type_180==1
		if Dwell_Type==14:
			Dwell_Type_190==1
		Zone_Class=request.form['Zone_Class']
		Zone_Class_FV=0
		Zone_Class_RH=0
		Zone_Class_RL=0
		Zone_Class_RM=0
		if Zone_Class==1:
			Zone_Class_FV==1
		if Zone_Class==2:
			Zone_Class_RH==1
		if Zone_Class==3:
			Zone_Class_RL==1
		if Zone_Class==4:
			Zone_Class_RM==1
		Neighborhood=request.form['Neighborhood']
		Neighborhood_Blueste=0
		Neighborhood_BrDale=0
		Neighborhood_BrkSide=0
		Neighborhood_ClearCr=0
		Neighborhood_CollgCr=0
		Neighborhood_Crawfor=0
		Neighborhood_Edwards=0
		Neighborhood_Gilbert=0
		Neighborhood_IDOTRR=0
		Neighborhood_MeadowV=0
		Neighborhood_Mitchel=0
		Neighborhood_NAmes=0
		Neighborhood_NPkVill=0
		Neighborhood_NWAmes=0
		Neighborhood_NoRidge=0
		Neighborhood_NridgHt=0
		Neighborhood_OldTown=0
		Neighborhood_SWISU=0
		Neighborhood_Sawyer=0
		Neighborhood_SawyerW=0
		Neighborhood_Somerst=0
		Neighborhood_StoneBr=0
		Neighborhood_Timber=0
		Neighborhood_Veenker=0
		if Neighborhood==1:
			Neighborhood_Blueste==1
		if Neighborhood==2:
			Neighborhood_BrDale==1
		if Neighborhood==3:
			Neighborhood_BrkSide==1
		if Neighborhood==4:
			Neighborhood_ClearCr==1
		if Neighborhood==5:
			Neighborhood_CollgCr==1
		if Neighborhood==6:
			Neighborhood_Crawfor==1
		if Neighborhood==7:
			Neighborhood_Edwards==1
		if Neighborhood==8:
			Neighborhood_Gilbert==1
		if Neighborhood==9:
			Neighborhood_IDOTRR==1
		if Neighborhood==10:
			Neighborhood_MeadowV==1
		if Neighborhood==11:
			Neighborhood_Mitchel==1
		if Neighborhood==12:
			Neighborhood_NAmes==1
		if Neighborhood==13:
			Neighborhood_NPkVill==1
		if Neighborhood==14:
			Neighborhood_NWAmes==1
		if Neighborhood==15:
			Neighborhood_NoRidge==1
		if Neighborhood==16:
			Neighborhood_NridgHt==1
		if Neighborhood==17:
			Neighborhood_OldTown==1
		if Neighborhood==18:
			Neighborhood_SWISU==1
		if Neighborhood==19:
			Neighborhood_Sawyer==1
		if Neighborhood==20:
			Neighborhood_SawyerW==1
		if Neighborhood==21:
			Neighborhood_Somerst==1
		if Neighborhood==22:
			Neighborhood_StoneBr==1
		if Neighborhood==23:
			Neighborhood_Timber==1
		if Neighborhood==24:
			Neighborhood_Veenker==1
		Exterior1st=request.form['Exterior1st']
		Exterior1st_AsphShn=0
		Exterior1st_BrkComm=0
		Exterior1st_BrkFace=0
		Exterior1st_CBlock=0
		Exterior1st_CemntBd=0
		Exterior1st_HdBoard=0
		Exterior1st_ImStucc=0
		Exterior1st_MetalSd=0
		Exterior1st_Plywood=0
		Exterior1st_Stone=0
		Exterior1st_Stucco=0
		Exterior1st_VinylSd=0
		Exterior1st_Wd_Sdng=0
		Exterior1st_WdShing=0
		if Exterior1st==1:
			Exterior1st_AsphShn==1
		if Exterior1st==2:
			Exterior1st_BrkComm==1
		if Exterior1st==3:
			Exterior1st_BrkFace==1
		if Exterior1st==4:
			Exterior1st_CBlock==1
		if Exterior1st==5:
			Exterior1st_CemntBd==1
		if Exterior1st==6:
			Exterior1st_HdBoard==1
		if Exterior1st==7:
			Exterior1st_ImStucc==1
		if Exterior1st==8:
			Exterior1st_MetalSd==1
		if Exterior1st==9:
			Exterior1st_Plywood==1
		if Exterior1st==10:
			Exterior1st_Stone==1
		if Exterior1st==11:
			Exterior1st_Stucco==1
		if Exterior1st==12:
			Exterior1st_VinylSd==1
		if Exterior1st==13:
			Exterior1st_Wd_Sdng==1
		if Exterior1st==14:
			Exterior1st_WdShing==1
		BsmtExposure=request.form['BsmtExposure']
		BsmtExposure_Gd=0
		BsmtExposure_Mn=0
		BsmtExposure_No=0
		BsmtExposure_No_Basement=0
		if BsmtExposure==1:
			BsmtExposure_Gd==1
		if BsmtExposure==2:
			BsmtExposure_Mn==1
		if BsmtExposure==3:
			BsmtExposure_No==1
		if BsmtExposure==4:
			BsmtExposure_No_Basement==1
		CentralAir=request.form['CentralAir']
		CentralAir_Y=0
		if CentralAir==1:
			CentralAir_Y==1
		KitchenQual=request.form['KitchenQual']
		KitchenQual_Fa=0
		KitchenQual_Gd=0
		KitchenQual_TA=0
		if KitchenQual==1:
			KitchenQual_Fa==1
		if KitchenQual==2:
			KitchenQual_Gd==1
		if KitchenQual==3:
			KitchenQual_TA==1
		Functional=request.form['Functional']
		Functional_Maj2=0
		Functional_Min1=0
		Functional_Min2=0
		Functional_Mod=0
		Functional_Sev=0
		Functional_Typ=0
		if Functional==1:
			Functional_Maj2==1
		if Functional==2:
			Functional_Min1==1
		if Functional==3:
			Functional_Min2==1
		if Functional==4:
			Functional_Mod==1
		if Functional==5:
			Functional_Sev==1
		if Functional==6:
			Functional_Typ==1
		SaleType=request.form['SaleType']
		SaleType_CWD=0
		SaleType_Con=0
		SaleType_ConLD=0
		SaleType_ConLI=0
		SaleType_ConLw=0
		SaleType_New=0
		SaleType_Oth=0
		SaleType_WD=0
		if SaleType==1:
			SaleType_CWD==1
		if SaleType==2:
			SaleType_Con==1
		if SaleType==3:
			SaleType_ConLD==1
		if SaleType==4:
			SaleType_ConLI==1
		if SaleType==5:
			SaleType_ConLw==1
		if SaleType==6:
			SaleType_New==1
		if SaleType==7:
			SaleType_Oth==1
		if SaleType==8:
			SaleType_WD==1

		features=[YearBuilt, YearRemodAdd, BsmtFullBath, KitchenAbvGr,
       Fireplaces, GarageCars, Total_SF, OverallQual, OverallCond,
       Dwell_Type_30, Dwell_Type_40, Dwell_Type_45, Dwell_Type_50,
       Dwell_Type_60, Dwell_Type_70, Dwell_Type_75, Dwell_Type_80,
       Dwell_Type_85, Dwell_Type_90, Dwell_Type_120, Dwell_Type_160,
       Dwell_Type_180, Dwell_Type_190, Zone_Class_FV, Zone_Class_RH,
       Zone_Class_RL, Zone_Class_RM, Neighborhood_Blueste,
       Neighborhood_BrDale, Neighborhood_BrkSide,Neighborhood_ClearCr,
       Neighborhood_CollgCr, Neighborhood_Crawfor, Neighborhood_Edwards,
       Neighborhood_Gilbert,Neighborhood_IDOTRR, Neighborhood_MeadowV,
       Neighborhood_Mitchel,Neighborhood_NAmes, Neighborhood_NPkVill,
       Neighborhood_NWAmes, Neighborhood_NoRidge, Neighborhood_NridgHt,
       Neighborhood_OldTown, Neighborhood_SWISU, Neighborhood_Sawyer,
       Neighborhood_SawyerW, Neighborhood_Somerst, Neighborhood_StoneBr,
       Neighborhood_Timber, Neighborhood_Veenker, Exterior1st_AsphShn,
       Exterior1st_BrkComm, Exterior1st_BrkFace, Exterior1st_CBlock,
       Exterior1st_CemntBd, Exterior1st_HdBoard, Exterior1st_ImStucc,
       Exterior1st_MetalSd, Exterior1st_Plywood, Exterior1st_Stone,
       Exterior1st_Stucco, Exterior1st_VinylSd, Exterior1st_Wd_Sdng,
       Exterior1st_WdShing, BsmtExposure_Gd, BsmtExposure_Mn,
       BsmtExposure_No, BsmtExposure_No_Basement, CentralAir_Y,
       KitchenQual_Fa, KitchenQual_Gd, KitchenQual_TA, Functional_Maj2,
       Functional_Min1, Functional_Min2, Functional_Mod,
       Functional_Sev, Functional_Typ, SaleType_CWD, SaleType_Con,
       SaleType_ConLD, SaleType_ConLI, SaleType_ConLw, SaleType_New,
       SaleType_Oth, SaleType_WD]


		lst=map(lambda x: float(x), features)
		values=np.array(list(lst))
		values=values.reshape(1,-1)
		pred=model.predict(values)

		return render_template("result.html", pred=pred)

		
if __name__=='__main__':
	app.run(debug=True)