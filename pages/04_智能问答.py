import streamlit as st

st.set_page_config(page_title="智能问答助手", layout="wide")
st.markdown("📍 当前流程节点：智能问答助手（第 4 步 / 共 4 步）")
st.title("💡 智能问答助手")

# 获取当前上下文客户
client = st.session_state.get("active_client")
if client:
    st.markdown(f"🧾 当前尽调客户：**{client}**")

st.markdown("本模块用于快速提问、获取产业 / 客户 / 政策等知识型结构化问答结果。")

# 初始化聊天记录结构
if "qa_chat_history" not in st.session_state:
    st.session_state.qa_chat_history = []  # 每条为 (问题, 回答, 来源)

# 输入问题
st.markdown("---")
st.subheader("🔍 提问区")
query = st.text_input("请输入您的问题（如：该公司是否享受政策补贴？）", key="qa_input")

if query:
    # 模拟回答逻辑
    if "融资" in query:
        answer = "该公司在2024年完成C轮融资，金额约为5亿元人民币。"
        source = "企业融资数据 · 知识库"
    elif "政策" in query:
        answer = "根据北京市2023年智能制造专项资金，该公司属于支持范围内。"
        source = "北京产业政策库 · 政策编号[2023-智能-12]"
    elif "客户" in query or "结构" in query:
        answer = "该公司客户结构以高校和医院为主，B端客户占比超过80%。"
        source = "企业销售结构分析 · 企业画像"
    else:
        answer = "该问题暂未识别为已训练知识点，可联系后台补充数据。"
        source = "未知来源"

    # 保存到聊天记录
    st.session_state.qa_chat_history.append((query, answer, source))

# 展示历史问答记录
st.markdown("---")
st.subheader("📋 问答历史记录")

if st.session_state.qa_chat_history:
    for i, (q, a, src) in enumerate(st.session_state.qa_chat_history[::-1]):
        st.markdown(f"**Q{i+1}: {q}**")
        st.markdown(f"🧠 回答：{a}")
        st.markdown(f"<div style='color:gray;font-size:13px;margin-top:0px;'>📎 来源：{src}</div>", unsafe_allow_html=True)
        st.markdown("---")
else:
    st.info("暂无问答记录。")

# 清空按钮
if st.button("🧹 清空问答记录"):
    st.session_state.qa_chat_history = []
    st.success("问答记录已清空")