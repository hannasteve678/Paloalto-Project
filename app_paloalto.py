import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="PAN Workforce Intelligence", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Inter:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

html,body,[class*="css"],.stApp{font-family:'Inter',sans-serif!important;background:#FFFFFF!important;color:#1A1A1A!important;}
.stApp,.block-container{background:#FFFFFF!important;padding-top:0!important;max-width:100%!important;padding-left:0!important;padding-right:0!important;}
[data-testid="collapsedControl"]{display:none!important;}
section[data-testid="stSidebar"]{display:none!important;}

[data-testid="stMetricLabel"] p{font-family:'Inter',sans-serif!important;font-size:0.60rem!important;font-weight:600!important;letter-spacing:0.08em!important;text-transform:uppercase!important;color:#6B7280!important;}
[data-testid="stMetricValue"]>div{font-family:'Space Mono',monospace!important;font-size:1.4rem!important;color:#111827!important;font-weight:700!important;}
[data-testid="stMetricDelta"] svg{display:none!important;}
[data-testid="stMetricDelta"]>div{font-size:0.65rem!important;color:#9CA3AF!important;}
div[data-testid="stMetric"]{background:#F9FAFB!important;border:1px solid #E5E7EB!important;border-radius:8px!important;padding:16px 18px 12px!important;box-shadow:none!important;}

.stTabs [data-baseweb="tab-list"]{background:#FFFFFF!important;border-bottom:1.5px solid #E5E7EB!important;gap:0!important;padding:0!important;}
.stTabs [data-baseweb="tab"]{font-family:'Inter',sans-serif!important;font-size:0.75rem!important;font-weight:600!important;letter-spacing:0.04em!important;color:#9CA3AF!important;padding:12px 22px!important;border-bottom:2px solid transparent!important;margin-bottom:-1.5px!important;text-transform:uppercase!important;}
.stTabs [aria-selected="true"]{color:#111827!important;border-bottom:2px solid #E63946!important;}

.tag{display:block;font-family:'Inter',sans-serif;font-size:0.58rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#E63946;margin-bottom:5px;}
.h2{font-family:'Syne',sans-serif;font-size:1.15rem;font-weight:700;color:#111827;margin:0 0 14px;line-height:1.2;letter-spacing:-0.01em;}
.h3{font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:#111827;margin:0 0 10px;line-height:1.2;}
.note{font-family:'Inter',sans-serif;font-size:0.78rem;color:#6B7280;margin-bottom:16px;line-height:1.6;}
.rule{height:1px;background:#F3F4F6;margin:24px 0;}

.hero{background:linear-gradient(135deg,#111827 0%,#1F2937 100%);padding:40px 48px 36px;}
.hero-tag{font-family:'Inter',sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#6B7280;margin-bottom:16px;}
.hero-title{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;color:#F9FAFB;letter-spacing:-0.02em;line-height:1.08;margin-bottom:14px;}
.hero-sub{font-family:'Inter',sans-serif;font-size:0.80rem;color:#6B7280;font-style:italic;}
.hero-rate{padding:40px 36px;display:flex;flex-direction:column;justify-content:center;}
.hero-rate-val{font-family:'Space Mono',monospace;font-size:3.5rem;font-weight:700;line-height:1;}
.hero-rate-lbl{font-family:'Inter',sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;margin-top:8px;}
.hero-rate-sub{font-family:'Inter',sans-serif;font-size:0.70rem;margin-top:6px;}

.filter-wrap{background:#F9FAFB;border-bottom:1px solid #E5E7EB;padding:14px 40px;}
.filter-lbl{font-family:'Inter',sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#9CA3AF;margin-bottom:6px;}

.kpi-strip{display:grid;grid-template-columns:repeat(6,1fr);border-bottom:1px solid #E5E7EB;}
.kpi-cell{padding:18px 24px;border-right:1px solid #F3F4F6;}
.kpi-cell:last-child{border-right:none;}
.kpi-v{font-family:'Space Mono',monospace;font-size:1.35rem;font-weight:700;color:#111827;line-height:1;}
.kpi-l{font-family:'Inter',sans-serif;font-size:0.55rem;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#9CA3AF;margin-top:5px;}
.kpi-badge{display:inline-block;font-family:'Inter',sans-serif;font-size:0.52rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-top:4px;}

.card{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:8px;padding:20px;}
.card-red{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:8px;padding:20px;border-top:3px solid #E63946;}
.card-green{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:8px;padding:20px;border-top:3px solid #059669;}
.card-blue{background:#FFFFFF;border:1px solid #E5E7EB;border-radius:8px;padding:20px;border-top:3px solid #3B82F6;}

.cls-h{border-left:3px solid #E63946;padding:10px 14px;margin:5px 0;background:#FEF2F2;border-radius:0 4px 4px 0;}
.cls-m{border-left:3px solid #F59E0B;padding:10px 14px;margin:5px 0;background:#FFFBEB;border-radius:0 4px 4px 0;}
.cls-l{border-left:3px solid #059669;padding:10px 14px;margin:5px 0;background:#ECFDF5;border-radius:0 4px 4px 0;}
.cn{font-family:'Inter',sans-serif;font-weight:600;font-size:0.82rem;color:#111827;}
.cr{font-family:'Space Mono',monospace;font-size:0.80rem;float:right;font-weight:700;}
.cs{font-family:'Inter',sans-serif;font-size:0.65rem;color:#9CA3AF;clear:both;margin-top:2px;}

.rp{background:#111827;padding:28px;border-radius:8px;border:1px solid #374151;}
.rp-h{font-family:'Space Mono',monospace;font-size:3.5rem;font-weight:700;color:#F87171;line-height:1;}
.rp-m{font-family:'Space Mono',monospace;font-size:3.5rem;font-weight:700;color:#FCD34D;line-height:1;}
.rp-l{font-family:'Space Mono',monospace;font-size:3.5rem;font-weight:700;color:#6EE7B7;line-height:1;}
.rp-row{background:#1F2937;border-radius:4px;padding:9px 13px;margin:5px 0;font-size:0.76rem;color:#D1D5DB;border-left:2px solid #E63946;}
.rp-row span{float:right;font-family:'Space Mono',monospace;color:#F87171;}

.tbox{padding:20px;border-radius:8px;border:1px solid #E5E7EB;margin-bottom:12px;}
.tv{font-family:'Space Mono',monospace;font-size:1.6rem;font-weight:700;color:#111827;}
.tl{font-family:'Inter',sans-serif;font-size:0.58rem;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;color:#9CA3AF;margin-bottom:5px;}
.ts{font-family:'Inter',sans-serif;font-size:0.68rem;color:#9CA3AF;margin-top:4px;}

details>summary p{font-size:0.84rem!important;font-weight:600!important;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("Palo_Alto_Networks.csv")
    df['AgeGroup']     = pd.cut(df['Age'], bins=[17,25,35,45,60], labels=['18-25','26-35','36-45','46-60'])
    df['TenureBucket'] = pd.cut(df['YearsAtCompany'], bins=[-1,2,5,10,20,40], labels=['0-2','3-5','6-10','11-20','20+'])
    df['DistanceBand'] = pd.cut(df['DistanceFromHome'], bins=[0,5,15,29], labels=['Near','Mid','Far'])
    df['EduLabel']     = df['Education'].map({1:'Below College',2:'College',3:'Bachelor',4:'Master',5:'Doctor'})
    return df

df = load_data()

def ct(h=300):
    return dict(
        plot_bgcolor='#FFFFFF', paper_bgcolor='#FFFFFF',
        font=dict(family='Inter, sans-serif', size=10, color='#374151'),
        xaxis=dict(showgrid=True, gridcolor='#F9FAFB', linecolor='#E5E7EB',
                   tickfont=dict(size=9, color='#9CA3AF', family='Inter')),
        yaxis=dict(showgrid=True, gridcolor='#F9FAFB', linecolor='#E5E7EB',
                   tickfont=dict(size=9, color='#9CA3AF', family='Inter')),
        legend=dict(font=dict(size=9, family='Inter'), bgcolor='rgba(0,0,0,0)', borderwidth=0),
        margin=dict(t=20, b=55, l=50, r=14), height=h,
    )

R='#E63946'; AM='#F59E0B'; GR='#059669'; BL='#3B82F6'; BK='#111827'
OVERALL = df['Attrition'].mean()*100

# ── HERO ─────────────────────────────────────
st.markdown(f"""
<div style="display:grid;grid-template-columns:1fr 280px;
            background:linear-gradient(135deg,#111827 0%,#1F2937 100%);">
    <div style="padding:44px 52px 40px;">
        <div style="font-family:'Inter',sans-serif;font-size:0.56rem;font-weight:600;
                    letter-spacing:0.16em;text-transform:uppercase;color:#6B7280;margin-bottom:18px;">
            Palo Alto Networks &nbsp;/&nbsp; Human Resources &nbsp;/&nbsp; Workforce Intelligence
        </div>
        <div style="font-family:'Syne',sans-serif;font-size:2.6rem;font-weight:800;
                    color:#F9FAFB;letter-spacing:-0.02em;line-height:1.05;margin-bottom:16px;">
            Workforce Attrition<br>Risk Analytics
        </div>
        <div style="font-family:'Inter',sans-serif;font-size:0.82rem;color:#6B7280;font-style:italic;">
            1,470 employees &nbsp;&middot;&nbsp; 31 attributes &nbsp;&middot;&nbsp; 3 departments &nbsp;&middot;&nbsp; 9 job roles
        </div>
    </div>
    <div style="background:#E63946;padding:44px 36px;display:flex;
                flex-direction:column;justify-content:center;">
        <div style="font-family:'Inter',sans-serif;font-size:0.56rem;font-weight:700;
                    letter-spacing:0.14em;text-transform:uppercase;color:rgba(0,0,0,0.4);margin-bottom:10px;">
            Overall Attrition
        </div>
        <div style="font-family:'Space Mono',monospace;font-size:3.2rem;
                    font-weight:700;color:#111827;line-height:1;">
            {OVERALL:.1f}%
        </div>
        <div style="font-family:'Inter',sans-serif;font-size:0.72rem;color:rgba(0,0,0,0.45);
                    margin-top:10px;border-top:1px solid rgba(0,0,0,0.15);padding-top:10px;">
            237 of 1,470 employees left
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FILTERS ──────────────────────────────────
st.markdown("<div class='filter-wrap'><div class='filter-lbl'>Filters</div></div>", unsafe_allow_html=True)
fc1,fc2,fc3,fc4,fc5,fc6 = st.columns(6)
with fc1: dept_sel = st.selectbox("Department", ['All']+sorted(df['Department'].unique().tolist()))
with fc2:
    role_opts = ['All']+sorted(df['JobRole'].unique().tolist()) if dept_sel=='All' else ['All']+sorted(df[df['Department']==dept_sel]['JobRole'].unique().tolist())
    role_sel = st.selectbox("Job Role", role_opts)
with fc3: ot_sel = st.selectbox("Overtime", ['All','Yes','No'])
with fc4: travel_sel = st.selectbox("Business Travel", ['All','Travel_Frequently','Travel_Rarely','Non-Travel'])
with fc5: gender_sel = st.selectbox("Gender", ['All','Male','Female'])
with fc6: tenure_rng = st.slider("Tenure (Years)", 0, 40, (0,40))

dff = df.copy()
if dept_sel   != 'All': dff = dff[dff['Department']    == dept_sel]
if role_sel   != 'All': dff = dff[dff['JobRole']        == role_sel]
if ot_sel     != 'All': dff = dff[dff['OverTime']       == ot_sel]
if travel_sel != 'All': dff = dff[dff['BusinessTravel'] == travel_sel]
if gender_sel != 'All': dff = dff[dff['Gender']         == gender_sel]
dff = dff[(dff['YearsAtCompany']>=tenure_rng[0])&(dff['YearsAtCompany']<=tenure_rng[1])]

total=len(dff); left=int(dff['Attrition'].sum()); retained=total-left
rate=(left/total*100) if total>0 else 0
ot_rate=dff[dff['OverTime']=='Yes']['Attrition'].mean()*100 if len(dff[dff['OverTime']=='Yes'])>0 else 0
early_r=dff[dff['YearsAtCompany']<=2]['Attrition'].mean()*100 if len(dff[dff['YearsAtCompany']<=2])>0 else 0
avg_ten=dff[dff['Attrition']==1]['YearsAtCompany'].mean() if left>0 else 0
rl="CRITICAL" if rate>20 else ("ELEVATED" if rate>15 else "HEALTHY")
rc=R if rate>20 else (AM if rate>15 else GR)
badge_bg = "#FEF2F2" if rate>20 else ("#FFFBEB" if rate>15 else "#ECFDF5")
badge_c  = "#B91C1C" if rate>20 else ("#92400E" if rate>15 else "#065F46")

# ── KPI STRIP ────────────────────────────────
st.markdown(f"""
<div class="kpi-strip">
    <div class="kpi-cell">
        <div class="kpi-v" style="color:{rc};">{rate:.1f}%</div>
        <div class="kpi-l">Attrition Rate</div>
        <div class="kpi-badge" style="background:{badge_bg};color:{badge_c};">{rl}</div>
    </div>
    <div class="kpi-cell"><div class="kpi-v">{left:,}</div><div class="kpi-l">Employees Left</div></div>
    <div class="kpi-cell"><div class="kpi-v">{retained:,}</div><div class="kpi-l">Retained</div></div>
    <div class="kpi-cell"><div class="kpi-v">{ot_rate:.1f}%</div><div class="kpi-l">Overtime Risk Rate</div></div>
    <div class="kpi-cell"><div class="kpi-v">{early_r:.1f}%</div><div class="kpi-l">Early Tenure Loss</div></div>
    <div class="kpi-cell"><div class="kpi-v">{avg_ten:.1f} yrs</div><div class="kpi-l">Avg Tenure — Leavers</div></div>
</div>""", unsafe_allow_html=True)

st.write("")
T1,T2,T3,T4,T5 = st.tabs(["Overview","Risk Hotspots","Demographics","Workload","Live Tools"])

# ══ TAB 1 ════════════════════════════════════
with T1:
    st.write("")
    # Full-width dept
    st.markdown('<span class="tag">Department Attrition</span><p class="h2">Which Department Has the Highest Exit Rate?</p>', unsafe_allow_html=True)
    dept_d = dff.groupby('Department')['Attrition'].agg(['sum','count','mean']).reset_index()
    dept_d['Rate'] = (dept_d['mean']*100).round(1)
    dept_d = dept_d.sort_values('Rate',ascending=False)
    colors = [R if r>20 else AM if r>15 else GR for r in dept_d['Rate']]
    fig = go.Figure(go.Bar(x=dept_d['Department'], y=dept_d['Rate'],
                           marker_color=colors, marker_line_width=0,
                           text=[f"{r}%" for r in dept_d['Rate']], textposition='outside',
                           textfont=dict(size=15,family='Space Mono',color=BK), width=0.3))
    fig.add_hline(y=OVERALL, line_dash='dot', line_color='#D1D5DB', line_width=1.5,
                  annotation_text=f"Org Avg {OVERALL:.1f}%",
                  annotation_font=dict(size=9,color='#9CA3AF'))
    layout = ct(200)
    layout['yaxis']['title'] = 'Attrition Rate (%)'
    layout['yaxis']['range'] = [0, dept_d['Rate'].max()+12]
    layout['xaxis']['tickfont'] = dict(size=12,family='Inter',color=BK,weight=600)
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

    ca, cb = st.columns([2,3])
    with ca:
        st.markdown('<span class="tag">Composition</span><p class="h2">Retained vs Left</p>', unsafe_allow_html=True)
        fig = go.Figure(go.Pie(
            labels=['Left','Retained'], values=[left,retained], hole=0.62,
            marker=dict(colors=[R,GR], line=dict(color='#FFFFFF',width=4)),
            textinfo='percent', textfont=dict(size=12,family='Space Mono')
        ))
        fig.add_annotation(text=f"<b>{rate:.1f}%</b>", x=0.5, y=0.5, showarrow=False,
                           font=dict(size=22,color=BK,family='Space Mono'))
        fig.update_layout(height=250, paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                          showlegend=True,
                          legend=dict(orientation='h',y=-0.08,x=0.25,font=dict(size=10,family='Inter')),
                          margin=dict(t=10,b=45,l=10,r=10))
        st.plotly_chart(fig, use_container_width=True)

    with cb:
        st.markdown('<span class="tag">Income Distribution</span><p class="h2">Lower Earners Exit More</p>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=dff[dff['Attrition']==1]['MonthlyIncome'], name='Leavers',
                                   marker_color=R, opacity=0.7, nbinsx=18, histnorm='percent'))
        fig.add_trace(go.Histogram(x=dff[dff['Attrition']==0]['MonthlyIncome'], name='Stayers',
                                   marker_color=GR, opacity=0.7, nbinsx=18, histnorm='percent'))
        layout = ct(250)
        layout['barmode'] = 'overlay'
        layout['xaxis']['title'] = 'Monthly Income ($)'
        layout['yaxis']['title'] = '% of Group'
        layout['legend'] = dict(orientation='h',y=-0.22,x=0.3,font=dict(size=10,family='Inter'))
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

    cr1, cr2 = st.columns(2)
    with cr1:
        st.markdown('<span class="tag">Satisfaction Radar</span><p class="h2">How Leavers Feel vs Stayers</p>', unsafe_allow_html=True)
        cats=['Job Sat.','Environment','Work-Life','Relationships','Job Inv.']
        keys=['JobSatisfaction','EnvironmentSatisfaction','WorkLifeBalance','RelationshipSatisfaction','JobInvolvement']
        lv=[dff[dff['Attrition']==1][k].mean() for k in keys]
        sv=[dff[dff['Attrition']==0][k].mean() for k in keys]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=lv+[lv[0]],theta=cats+[cats[0]],fill='toself',name='Leavers',line_color=R,fillcolor='rgba(230,57,70,0.10)'))
        fig.add_trace(go.Scatterpolar(r=sv+[sv[0]],theta=cats+[cats[0]],fill='toself',name='Stayers',line_color=GR,fillcolor='rgba(5,150,105,0.10)'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0,4],tickfont=dict(size=8,family='Space Mono'))),
                          showlegend=True,height=270,paper_bgcolor='#FFFFFF',
                          font=dict(family='Inter',size=10),
                          legend=dict(orientation='h',y=-0.10,x=0.32,font=dict(size=10,family='Inter')),
                          margin=dict(t=20,b=50,l=40,r=40))
        st.plotly_chart(fig, use_container_width=True)

    with cr2:
        st.markdown('<span class="tag">Seniority</span><p class="h2">Entry Roles Carry the Most Risk</p>', unsafe_allow_html=True)
        jl = dff.groupby('JobLevel')['Attrition'].mean().reset_index()
        jl['Rate'] = (jl['Attrition']*100).round(1)
        jl['L'] = jl['JobLevel'].map({1:'L1 Entry',2:'L2 Junior',3:'L3 Mid',4:'L4 Senior',5:'L5 Lead'})
        colors=[R if r>20 else AM if r>15 else GR for r in jl['Rate']]
        fig = go.Figure(go.Bar(x=jl['L'],y=jl['Rate'],marker_color=colors,marker_line_width=0,
                               text=[f"{r}%" for r in jl['Rate']],textposition='outside',
                               textfont=dict(size=11,family='Space Mono',color=BK),width=0.45))
        fig.add_hline(y=OVERALL,line_dash='dot',line_color='#D1D5DB',line_width=1.5)
        layout=ct(270); layout['yaxis']['title']='Attrition (%)'; layout['yaxis']['range']=[0,jl['Rate'].max()+12]
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)

# ══ TAB 2 ════════════════════════════════════
with T2:
    st.write("")
    st.markdown('<span class="tag">Heatmap</span><p class="h2">Attrition Intensity — Role × Department</p>', unsafe_allow_html=True)
    hm = dff.groupby(['Department','JobRole'])['Attrition'].mean().reset_index()
    hm['Rate'] = (hm['Attrition']*100).round(1)
    pivot = hm.pivot(index='JobRole',columns='Department',values='Rate').fillna(0)
    fig = go.Figure(go.Heatmap(
        z=pivot.values,x=pivot.columns.tolist(),y=pivot.index.tolist(),
        colorscale=[[0,'#F0FDF4'],[0.4,'#FEF3C7'],[0.7,'#FED7AA'],[1,'#FEE2E2']],
        text=[[f"{v:.0f}%" if v>0 else "—" for v in row] for row in pivot.values],
        texttemplate="%{text}",textfont=dict(size=12,family='Space Mono',color='#111827'),
        colorbar=dict(title='%',tickfont=dict(size=9,family='Inter')),
    ))
    layout=ct(300); layout['margin']=dict(t=20,b=60,l=200,r=20)
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

    cb1,cb2 = st.columns([3,2])
    with cb1:
        st.markdown('<span class="tag">Role Rankings</span><p class="h2">Exit Rate per Job Role</p>', unsafe_allow_html=True)
        role_d = dff.groupby('JobRole')['Attrition'].agg(['sum','count','mean']).reset_index()
        role_d['Rate'] = (role_d['mean']*100).round(1)
        role_d.columns=['Role','Left','Total','Mean','Rate']
        role_d = role_d.sort_values('Rate',ascending=True)
        colors=[R if r>25 else AM if r>15 else GR for r in role_d['Rate']]
        fig = go.Figure(go.Bar(x=role_d['Rate'],y=role_d['Role'],orientation='h',
                               marker_color=colors,marker_line_width=0,
                               text=[f"{r}%" for r in role_d['Rate']],textposition='outside',
                               textfont=dict(size=10,family='Space Mono',color=BK)))
        fig.add_vline(x=OVERALL,line_dash='dot',line_color='#D1D5DB',line_width=1.5,
                      annotation_text="Avg",annotation_font=dict(size=9,color='#9CA3AF'))
        layout=ct(370); layout['xaxis']['title']='Attrition Rate (%)'; layout['xaxis']['range']=[0,role_d['Rate'].max()+10]
        layout['margin']=dict(t=20,b=55,l=190,r=14)
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)

    with cb2:
        st.markdown('<span class="tag">Risk Tiers</span><p class="h2">Role Classification</p>', unsafe_allow_html=True)
        st.write("")
        high=role_d[role_d['Rate']>25].sort_values('Rate',ascending=False)
        mid=role_d[(role_d['Rate']>15)&(role_d['Rate']<=25)].sort_values('Rate',ascending=False)
        low=role_d[role_d['Rate']<=15].sort_values('Rate',ascending=False)
        for _,r in high.iterrows():
            st.markdown(f'<div class="cls-h"><span class="cn">{r["Role"]}</span><span class="cr" style="color:{R};">{r["Rate"]}%</span><div class="cs">{int(r["Left"])} of {int(r["Total"])} left &bull; High Risk</div></div>',unsafe_allow_html=True)
        for _,r in mid.iterrows():
            st.markdown(f'<div class="cls-m"><span class="cn">{r["Role"]}</span><span class="cr" style="color:{AM};">{r["Rate"]}%</span><div class="cs">{int(r["Left"])} of {int(r["Total"])} left &bull; Moderate</div></div>',unsafe_allow_html=True)
        for _,r in low.iterrows():
            st.markdown(f'<div class="cls-l"><span class="cn">{r["Role"]}</span><span class="cr" style="color:{GR};">{r["Rate"]}%</span><div class="cs">{int(r["Left"])} of {int(r["Total"])} left &bull; Low Risk</div></div>',unsafe_allow_html=True)

# ══ TAB 3 ════════════════════════════════════
with T3:
    st.write("")
    st.markdown('<span class="tag">Demographics</span><p class="h2">Who Is Leaving?</p>', unsafe_allow_html=True)
    d1,d2,d3 = st.columns(3)
    for col_w, grp_col, title in [(d1,'AgeGroup','By Age Group'),(d2,'MaritalStatus','By Marital Status'),(d3,'Gender','By Gender')]:
        with col_w:
            gd=dff.groupby(grp_col,observed=True)['Attrition'].mean().reset_index()
            gd['Rate']=(gd['Attrition']*100).round(1)
            if grp_col=='MaritalStatus': gd=gd.sort_values('Rate',ascending=False)
            colors=[R if r>20 else AM if r>15 else GR for r in gd['Rate']]
            fig=go.Figure(go.Bar(x=gd[grp_col].astype(str),y=gd['Rate'],marker_color=colors,marker_line_width=0,
                                 text=[f"{r}%" for r in gd['Rate']],textposition='outside',
                                 textfont=dict(size=10,family='Space Mono',color=BK),width=0.45))
            fig.add_hline(y=OVERALL,line_dash='dot',line_color='#D1D5DB',line_width=1)
            layout=ct(250); layout['yaxis']['range']=[0,gd['Rate'].max()+12]
            layout['title']=dict(text=title,font=dict(family='Syne',size=12,color=BK,weight=700))
            fig.update_layout(**layout)
            st.plotly_chart(fig,use_container_width=True)

    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    st.markdown('<span class="tag">Education</span><p class="h2">Field of Study vs Exit Rate</p>', unsafe_allow_html=True)
    ef_d=dff.groupby('EducationField')['Attrition'].mean().reset_index()
    ef_d['Rate']=(ef_d['Attrition']*100).round(1)
    ef_d=ef_d.sort_values('Rate',ascending=True)
    colors=[R if r>20 else AM if r>15 else GR for r in ef_d['Rate']]
    fig=go.Figure(go.Bar(x=ef_d['Rate'],y=ef_d['EducationField'],orientation='h',
                         marker_color=colors,marker_line_width=0,
                         text=[f"{r}%" for r in ef_d['Rate']],textposition='outside',
                         textfont=dict(size=11,family='Space Mono',color=BK),width=0.55))
    fig.add_vline(x=OVERALL,line_dash='dot',line_color='#D1D5DB',line_width=1.5)
    layout=ct(200); layout['xaxis']['title']='Attrition Rate (%)'; layout['xaxis']['range']=[0,ef_d['Rate'].max()+8]
    layout['margin']=dict(t=16,b=50,l=140,r=14)
    fig.update_layout(**layout)
    st.plotly_chart(fig,use_container_width=True)

# ══ TAB 4 ════════════════════════════════════
with T4:
    st.write("")
    st.markdown('<span class="tag">Tenure Analysis</span><p class="h2">The First Two Years Are the Riskiest</p>', unsafe_allow_html=True)
    ten_d=dff.groupby('TenureBucket',observed=True)['Attrition'].mean().reset_index()
    ten_d['Rate']=(ten_d['Attrition']*100).round(1)
    colors=[R if r>20 else AM if r>15 else GR for r in ten_d['Rate']]
    fig=go.Figure(go.Bar(x=ten_d['TenureBucket'].astype(str),y=ten_d['Rate'],marker_color=colors,marker_line_width=0,
                         text=[f"{r}%" for r in ten_d['Rate']],textposition='outside',
                         textfont=dict(size=13,family='Space Mono',color=BK),width=0.4))
    fig.add_hline(y=OVERALL,line_dash='dot',line_color='#D1D5DB',line_width=1.5,
                  annotation_text=f"Org Avg {OVERALL:.1f}%",annotation_font=dict(size=9,color='#9CA3AF'))
    layout=ct(210); layout['yaxis']['title']='Attrition Rate (%)'; layout['yaxis']['range']=[0,ten_d['Rate'].max()+14]
    fig.update_layout(**layout)
    st.plotly_chart(fig,use_container_width=True)

    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    st.markdown('<span class="tag">Workload Factors</span>', unsafe_allow_html=True)
    w1,w2,w3 = st.columns(3)
    for col_w, grp_col, title in [(w1,'OverTime','Overtime Effect'),(w2,'BusinessTravel','Travel Burden'),(w3,'DistanceBand','Distance from Home')]:
        with col_w:
            wd=dff.groupby(grp_col,observed=True)['Attrition'].mean().reset_index()
            wd['Rate']=(wd['Attrition']*100).round(1)
            if grp_col=='BusinessTravel': wd=wd.sort_values('Rate',ascending=False)
            c2=[R if (v=='Yes' if grp_col=='OverTime' else r>20) else AM if r>15 else GR
                for v,r in zip(wd[grp_col].astype(str),wd['Rate'])]
            fig=go.Figure(go.Bar(x=wd[grp_col].astype(str),y=wd['Rate'],marker_color=c2,marker_line_width=0,
                                 text=[f"{r}%" for r in wd['Rate']],textposition='outside',
                                 textfont=dict(size=11,family='Space Mono',color=BK),width=0.4))
            fig.add_hline(y=OVERALL,line_dash='dot',line_color='#D1D5DB',line_width=1)
            layout=ct(250); layout['yaxis']['range']=[0,wd['Rate'].max()+14]
            layout['title']=dict(text=title,font=dict(family='Syne',size=12,color=BK))
            layout['xaxis']['tickangle']=-10
            fig.update_layout(**layout)
            st.plotly_chart(fig,use_container_width=True)

# ══ TAB 5 ════════════════════════════════════
with T5:
    st.write("")
    RT1,RT2,RT3 = st.tabs(["Risk Profiler","Cost Calculator","What-If Simulator"])

    with RT1:
        st.markdown('<span class="tag">Live Tool 01</span><p class="h2">Employee Attrition Risk Profiler</p>', unsafe_allow_html=True)
        st.markdown('<p class="note">Enter an employee profile to instantly score their attrition risk based on real patterns in the dataset.</p>', unsafe_allow_html=True)
        cf,cr = st.columns(2)
        with cf:
            p_age=st.slider("Age",18,60,28); p_tenure=st.slider("Years at Company",0,40,1)
            p_ot=st.selectbox("Works Overtime",["Yes","No"]); p_travel=st.selectbox("Business Travel",["Travel_Frequently","Travel_Rarely","Non-Travel"])
            p_jsat=st.slider("Job Satisfaction (1–4)",1,4,2); p_env=st.slider("Environment Satisfaction (1–4)",1,4,2)
            p_wlb=st.slider("Work-Life Balance (1–4)",1,4,2); p_income=st.slider("Monthly Income ($)",1000,20000,3000,500)
            p_promo=st.slider("Years Since Last Promotion",0,15,5)
            p_jlevel=st.selectbox("Job Level",[1,2,3,4,5],format_func=lambda x:{1:"L1 Entry",2:"L2 Junior",3:"L3 Mid",4:"L4 Senior",5:"L5 Lead"}[x])
        with cr:
            risk=0.0; drivers=[]
            if p_ot=="Yes": risk+=28; drivers.append(("Works Overtime","+28"))
            else: risk+=5
            if p_age<=25: risk+=18; drivers.append(("Age 18–25 high-risk group","+18"))
            elif p_age<=35: risk+=8
            else: risk+=2
            if p_tenure<=2: risk+=16; drivers.append(("Early tenure 0–2 years","+16"))
            elif p_tenure<=5: risk+=6
            if p_travel=="Travel_Frequently": risk+=12; drivers.append(("Frequent business travel","+12"))
            elif p_travel=="Travel_Rarely": risk+=5
            if p_jsat==1: risk+=10; drivers.append(("Very low job satisfaction","+10"))
            elif p_jsat==2: risk+=5
            if p_env==1: risk+=8; drivers.append(("Low environment satisfaction","+8"))
            elif p_env==2: risk+=3
            if p_wlb==1: risk+=6; drivers.append(("Poor work-life balance","+6"))
            if p_income<df[df['Attrition']==1]['MonthlyIncome'].mean()*0.75: risk+=8; drivers.append(("Below-average income","+8"))
            if p_promo>=4: risk+=5; drivers.append(("Promotion stagnation 4+ yrs","+5"))
            if p_jlevel==1: risk+=5; drivers.append(("Entry-level position","+5"))
            risk=min(risk,99)
            if risk>=60: sc="rp-h"; rl2="HIGH RISK"; rc2="#EF4444"; adv="Immediate action. Schedule 1:1, review compensation, reduce workload."
            elif risk>=35: sc="rp-m"; rl2="MODERATE RISK"; rc2="#F59E0B"; adv="Monitor closely. Career development and flexibility options."
            else: sc="rp-l"; rl2="LOW RISK"; rc2="#059669"; adv="Stable. Regular check-ins and growth opportunities."
            rows_html='\n'.join([f'<div class="rp-row">{d[0]}<span>{d[1]}</span></div>' for d in drivers]) if drivers else '<p style="color:#6B7280;font-size:0.78rem;">No major risk factors detected.</p>'
            st.markdown(f'<div class="rp"><div style="font-family:Inter,sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#6B7280;margin-bottom:12px;">Attrition Risk Score</div><div class="{sc}">{risk:.0f}</div><div style="font-family:Inter,sans-serif;font-size:0.58rem;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;color:{rc2};margin-top:6px;">{rl2}</div><div style="height:1px;background:#374151;margin:16px 0 12px;"></div><div style="font-family:Inter,sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#6B7280;margin-bottom:8px;">Key Risk Drivers</div>{rows_html}<div style="height:1px;background:#374151;margin:14px 0;"></div><div style="font-family:Inter,sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#6B7280;margin-bottom:6px;">HR Recommendation</div><div style="font-family:Inter,sans-serif;font-size:0.78rem;color:#9CA3AF;line-height:1.6;">{adv}</div></div>', unsafe_allow_html=True)

    with RT2:
        st.markdown('<span class="tag">Live Tool 02</span><p class="h2">Attrition Financial Impact Calculator</p>', unsafe_allow_html=True)
        ci,co = st.columns(2)
        with ci:
            avg_sal=st.slider("Average Annual Salary ($)",30000,200000,72000,5000)
            rep_pct=st.slider("Replacement Cost (% of Salary)",50,200,100,10)
            ob_wks=st.slider("Weeks to Full Productivity",4,52,16,4)
            pl_pct=st.slider("Productivity Loss During Ramp (%)",10,80,40,5)
        with co:
            rc_=avg_sal*(rep_pct/100); pc_=(avg_sal/52)*ob_wks*(pl_pct/100); pl_=rc_+pc_; tc_=pl_*left; sv_=tc_*0.25
            st.markdown(f'<div class="tbox card-red"><div class="tl">Cost Per Leaver</div><div class="tv">${pl_:,.0f}</div><div class="ts">Replacement + ramp-up productivity loss</div></div><div class="tbox card-blue"><div class="tl">Total Attrition Cost</div><div style="font-family:Space Mono,monospace;font-size:1.6rem;font-weight:700;color:#3B82F6;">${tc_:,.0f}</div><div class="ts">Based on {left} leavers in current filtered view</div></div><div class="tbox card-green"><div class="tl">Savings at 25% Reduction</div><div style="font-family:Space Mono,monospace;font-size:1.6rem;font-weight:700;color:#059669;">${sv_:,.0f}</div><div class="ts">Achievable via targeted retention programs</div></div>', unsafe_allow_html=True)

    with RT3:
        st.markdown('<span class="tag">Live Tool 03</span><p class="h2">Retention What-If Simulator</p>', unsafe_allow_html=True)
        st.markdown('<p class="note">Adjust the levers below to simulate the impact of HR policy interventions on attrition.</p>', unsafe_allow_html=True)
        cs,cr2=st.columns(2)
        with cs:
            r_ot=st.slider("Reduce Overtime Workers by (%)",0,100,30)
            r_tr=st.slider("Reduce Frequent Travelers by (%)",0,100,20)
            r_sat=st.slider("Improve Job Satisfaction by (pts)",0.0,2.0,0.5,0.1)
            r_sal=st.slider("Salary Increase (%)",0,30,10)
        with cr2:
            ot_w=len(df[df['OverTime']=='Yes']); ot_ar=df[df['OverTime']=='Yes']['Attrition'].mean(); no_ar=df[df['OverTime']=='No']['Attrition'].mean()
            ft_w=len(df[df['BusinessTravel']=='Travel_Frequently']); ft_ar=df[df['BusinessTravel']=='Travel_Frequently']['Attrition'].mean(); rt_ar=df[df['BusinessTravel']=='Travel_Rarely']['Attrition'].mean()
            tot_red=max(0,ot_w*(r_ot/100)*(ot_ar-no_ar)+ft_w*(r_tr/100)*(ft_ar-rt_ar)+r_sat*8+r_sal*0.8)
            pj_left=max(0,left-tot_red); pj_rate=(pj_left/total*100) if total>0 else 0; saved=left-pj_left
            st.markdown(f'<div class="tbox card-green"><div class="tl">Projected Attrition Rate</div><div style="font-family:Space Mono,monospace;font-size:1.6rem;font-weight:700;color:#059669;">{pj_rate:.1f}%</div><div class="ts">Down from {rate:.1f}% &nbsp;/&nbsp; -{rate-pj_rate:.1f}% improvement</div></div><div class="tbox card-blue"><div class="tl">Additional Employees Retained</div><div style="font-family:Space Mono,monospace;font-size:1.6rem;font-weight:700;color:#3B82F6;">+{saved:.0f}</div><div class="ts">Would stay with these interventions</div></div>', unsafe_allow_html=True)
            st.write("")
            fig=go.Figure(go.Bar(x=['Current','Projected'],y=[rate,pj_rate],marker_color=[R,GR],marker_line_width=0,
                                 text=[f"{rate:.1f}%",f"{pj_rate:.1f}%"],textposition='outside',
                                 textfont=dict(size=13,family='Space Mono',color=BK),width=0.35))
            layout=ct(240); layout['yaxis']['range']=[0,max(rate,pj_rate)+12]; layout['margin']=dict(t=20,b=55,l=50,r=14)
            fig.update_layout(**layout); st.plotly_chart(fig,use_container_width=True)

with st.expander("View Filtered Employee Records"):
    st.markdown(f"<span style='font-family:Inter,sans-serif;font-size:0.70rem;font-weight:600;color:#9CA3AF;'>{len(dff):,} employees match current filters</span>", unsafe_allow_html=True)
    cols=['Age','Department','JobRole','Gender','MaritalStatus','YearsAtCompany','OverTime','BusinessTravel','MonthlyIncome','JobSatisfaction','Attrition']
    st.dataframe(dff[cols].reset_index(drop=True),use_container_width=True,height=250)
    st.download_button("Download CSV",dff.to_csv(index=False).encode('utf-8'),"PaloAlto_Filtered.csv","text/csv")

st.markdown('<div style="text-align:right;padding:16px 8px 6px;font-family:Inter,sans-serif;font-size:0.60rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#D1D5DB;">Palo Alto Networks &bull; Workforce Intelligence &bull; v1.0</div>', unsafe_allow_html=True)