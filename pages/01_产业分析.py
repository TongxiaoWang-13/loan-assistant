import streamlit as st
from docx import Document
import os
import time
import datetime
import tempfile

st.set_page_config(page_title="产业分析", layout="wide")

st.markdown("📍 当前流程节点：产业分析（第 1 步 / 共 4 步）")
st.title("📊 产业分析模块")

# ===== 页面头部功能区 =====
st.markdown("---")
st.subheader("📌 当前调研任务")
st.markdown("""
- **任务来源**：北京市2024年调研指令：围绕“万亿/千亿产业集群”进行深度分析。
- **调研目标**：形成行业分析报告 + 本地可服务客户列表。
- **参考优先级**：
  - 高优先：机器人 / 动力电池 / 商业航天 / 集成电路
  - 中优先：氢能 / 海洋装备 / 生物医药
  - 低优先：智慧农业 / 新型轨道交通
""")

st.markdown("---")
st.subheader("🔍 请选择调研产业")
industries = ["人形机器人", "动力电池", "商业航天", "集成电路", "氢能燃料", "智慧农业"]
selected = st.selectbox("已支持产业：", industries)

st.markdown("---")
st.subheader("📂 报告结构预览")
st.markdown("""
报告结构包括：
- 一、产业概要（1.1~1.10）
- 二、本地产业现状（2.1~2.3）
- 三、产业优质企业（3.1~3.3）
- 四、挑战与机遇（4.1~4.3）
""")

# ===== 文档解析结构加载 =====
current_dir = os.path.dirname(__file__)
doc_path = os.path.join(current_dir, "机器人产业报告.docx")

if not os.path.exists(doc_path):
    st.error("❌ 未找到 '机器人产业报告.docx'")
    st.stop()

doc = Document(doc_path)
paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

import re
section_pattern = re.compile(r"^([一二三四五六七八九十]+)、(.+)$")
subsection_pattern = re.compile(r"^(\d+(\.\d+)+)\s*(.*)$")

structure = {}
current_section = ""
current_sub = ""

for para in paragraphs:
    if section_pattern.match(para):
        current_section = para
        structure[current_section] = {}
    elif subsection_pattern.match(para):
        current_sub = para
        structure[current_section][current_sub] = []
    elif current_section and current_sub:
        structure[current_section][current_sub].append(para)

# ===== 动态生成每节的思维链内容 =====
def generate_dynamic_thinking_chain(title):
    if "定义" in title or "1.1" in title:
        return "本节旨在明确人形机器人产业边界和核心构成，帮助客户经理理解产品范围与应用界限。"
    elif "发展历程" in title:
        return "通过回顾发展历程，梳理技术更迭与政策演进脉络，为投资节奏判断提供参考。"
    elif "市场" in title or "规模" in title:
        return "市场数据用于评估产业潜力、制定服务客户策略及区域支持判断。"
    elif "本地" in title or "北京市" in title:
        return "本地现状判断有助于识别区域金融机会与政策兑现程度。"
    elif "企业" in title:
        return "本节对重点企业进行画像分析，便于挖掘服务对象与判断落地能力。"
    elif "挑战" in title:
        return "系统梳理技术瓶颈、商业落地难点，为银行授信与风控提供基础支撑。"
    elif "机遇" in title:
        return "从政策、市场、客户视角挖掘可操作性强的金融合作空间。"
    else:
        return "本节用于帮助客户经理理解产业趋势、判断政策导向与技术落点。"

# ===== 报告输出区：页签结构 + 折叠展示 + 自适应思维链 =====
st.markdown("---")
st.subheader("📄 报告画布（Tabs + 思维链优化）")

tabs = st.tabs(list(structure.keys()))

for tab, section_title in zip(tabs, structure.keys()):
    with tab:
        selected_section = structure[section_title]
        st.markdown(f"<h2 style='margin-top:1.2rem;color:#8B1A1A'>{section_title}</h2>", unsafe_allow_html=True)
        for sub_title, paras in selected_section.items():
            with st.expander(sub_title):
                st.markdown(
                    f"""
                    <div style='background-color:#F3F4F6;border-left:4px solid #8B1A1A;padding:10px;margin-bottom:12px;'>
                        🧠 <b>思维链推理：</b> {generate_dynamic_thinking_chain(sub_title)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                for para in paras:
                    st.markdown(f"<div style='font-size:16px;line-height:1.8;text-indent:2em;margin-bottom:0.5rem;'>{para}</div>", unsafe_allow_html=True)
                    time.sleep(0.3)
                st.markdown("<hr style='margin-top:1rem; margin-bottom:0.5rem;'>", unsafe_allow_html=True)
st.markdown("**✏ 提交修改建议：**")
edit = st.text_area("请输入修改建议", key=f"suggest_{sub_title}")
if st.button("提交", key=f"btn_{sub_title}"):
    st.success("✅ 修改建议已记录（模拟功能）")
