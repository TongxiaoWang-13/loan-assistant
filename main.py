# main.py - 首页跳转逻辑修复（使用英文名 + 去掉路径前缀）
import streamlit as st
import time

st.set_page_config(
    page_title="贷前作业智能助手系统",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.success("请选择以上的功能页面开始使用。")

# ============ 样式 ============
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #F9FAFB;
    font-family: 'Microsoft YaHei', sans-serif;
}
h1, h2, h3 {
    color: #8B1A1A;
    font-weight: 600;
}
p, li, div, .stMarkdown {
    color: #374151;
    font-size: 16px;
}
hr {
    border: none;
    border-top: 1px solid #E5E7EB;
    margin: 2rem 0;
}
.stButton>button {
    border: 1px solid #8B1A1A;
    color: #8B1A1A;
    background-color: white;
    padding: 6px 16px;
    border-radius: 6px;
}
.stButton>button:hover {
    background-color: #f3f4f6;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============ 顶部状态栏 ============
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🔔 **系统通知**：本系统为演示版，部分功能尚未接入真实接口。")
with col2:
    st.markdown("📌 **当前任务**：2024年度制造业客户尽调（负责人：张三）")
with col3:
    st.markdown("🧑‍💼 **登录用户**：pku_admin（产品经理）")
st.markdown("---")

# ============ 系统简介 ============
st.title("贷前作业智能助手系统")
st.subheader("系统概览")
st.markdown("""
本系统聚焦银行客户经理贷前尽调作业的数字化升级，支持从任务接收、产业理解、客户筛选、尽调执行到报告生成的全流程闭环。
通过融合大模型推理能力、结构化知识图谱与行业数据积累，为客户经理提供智能化、结构化、可追溯的尽调支持平台。
""")

# ============ 模块卡片 ============
st.markdown("---")
st.subheader("核心功能模块")
cols = st.columns(4)
modules = [
    ("产业分析", "识别重点行业，聚焦国家/地方政策、市场趋势与关键风险点。", "01_产业分析.py"),
    ("客户画像", "筛选优质客户，整合工商、产品、政策、招投标等信息，形成客户全景图。", "02_客户画像报告.py"),
    ("尽调助手", "问题清单生成、问答记录、智能建议、风险识别与报告导出，一站完成尽调任务。", "03_尽调助手.py"),
    ("问答助手", "随时提问，快速调取产业/客户/政策等信息内容，提升决策效率。", "04_智能问答.py")
]
for i, (name, desc, page_file) in enumerate(modules):
    with cols[i]:
        st.markdown(f"### {i+1}. {name}")
        st.markdown(f"<div style='font-size:15px; color:#4B5563;'>{desc}</div>", unsafe_allow_html=True)
        if st.button("进入模块", key=f"go_{i}_{name}"):
            st.switch_page(page_file)

# ============ 应用场景 ============
st.markdown("---")
st.subheader("典型应用场景")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**场景一：产业走访准备**")
    st.markdown("通过产业分析快速了解目标行业背景、政策支持方向与竞争格局，形成客户经理访谈提纲。")
with col2:
    st.markdown("**场景二：客户准入尽调**")
    st.markdown("客户画像+尽调助手辅助高效完成客户尽调，自动形成结构化报告与风险提示。")
with col3:
    st.markdown("**场景三：审批材料准备**")
    st.markdown("整合分析过程文档、问答记录与总结建议，支持贷前审批材料撰写与汇报。")

# ============ 系统部署方式 ============
st.markdown("---")
st.subheader("系统部署方式")
deploy_cols = st.columns(3)
with deploy_cols[0]:
    st.markdown("**公有云 API**")
    st.markdown("通过公有云接口快速接入我方模型与平台能力，适用于创新试点。")
with deploy_cols[1]:
    st.markdown("**私有化部署**")
    st.markdown("支持部署至行内服务器，保障数据安全、稳定对接已有风控系统。")
with deploy_cols[2]:
    st.markdown("**嵌入式组件**")
    st.markdown("可将问答、尽调报告等组件按模块接入至原有系统中，快速融合。")

# ============ 页脚 ============
st.markdown("---")
st.caption("© 智能贷前助手 · 内部演示系统 · 北京大学金融科技团队")
