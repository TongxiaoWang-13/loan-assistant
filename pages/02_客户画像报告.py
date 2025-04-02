import streamlit as st
import time
import altair as alt
import pandas as pd

st.set_page_config(page_title="客户画像报告", layout="wide")
st.markdown("📍 当前流程节点：客户画像报告（第 2 步 / 共 4 步）")
st.title("📌 客户画像报告模块")

# ===== ① 客户筛选入口区 =====
st.markdown("---")
st.subheader("🎯 客户筛选入口")
st.markdown("根据产业分析模块所选方向，自动推荐相关客户。")

industry_filter = st.selectbox("所属产业：", ["人形机器人", "工业机器人", "智能制造", "动力电池"])
region_filter = st.selectbox("客户地区：", ["不限", "北京", "杭州", "深圳"])
tag_filter = st.multiselect("客户标签筛选：", ["高潜客户", "政策扶持", "龙头企业", "本地落地"])

# ===== ② 客户卡片浏览区 =====
st.markdown("---")
st.subheader("🏢 客户列表（点击查看画像）")

clients = [
    {"名称": "杭州宇树科技有限公司", "标签": ["高潜客户", "政策扶持", "本地落地"], "概况": "专注人形机器人领域，已完成C轮融资"},
    {"名称": "北京星动纪元科技有限公司", "标签": ["本地落地"], "概况": "服务型机器人新锐企业，技术路线创新"},
    {"名称": "优必选科技股份有限公司", "标签": ["龙头企业"], "概况": "行业龙头，产品覆盖政务/教育/工业等"}
]

selected_client = None
for c in clients:
    match = all(tag in c["标签"] for tag in tag_filter)
    if region_filter != "不限" and region_filter not in c["名称"]:
        continue
    if not match:
        continue
    with st.container():
        st.markdown(f"### {c['名称']}")
        st.markdown(f"{c['概况']}")
        st.markdown(f"标签：{' '.join(['✅'+t for t in c['标签']])}")
        if st.button(f"📄 查看画像详情 - {c['名称']}"):
            selected_client = c["名称"]

# ===== ③ 多维画像展示区 =====
if selected_client:
    st.markdown("---")
    st.subheader(f"📊 {selected_client} - 多维画像详情")

    # 基本面 + 主营业务
    st.markdown("### 📋 企业基本面")
    col1, col2 = st.columns(2)
    with col1:
        st.write("注册资本：19248万元")
        st.write("成立时间：2016年6月")
        st.write("法定代表人：李明")
        st.write("统一社会信用代码：91330108MA2ZYJ5H56")
        st.write("企业评级：B+")
    with col2:
        st.write("员工规模：203人")
        st.write("企业性质：小型企业")
        st.write("行业领域：人形机器人")
        st.write("客户评价：优")

    st.markdown("### 🧠 主营业务与业务契机")
    st.markdown("- 主营：双足机器人控制系统、人形机器人整机、仿生驱动模块")
    st.markdown("- 发展契机：AI+硬件趋势推动人形机器人加速落地，政策支持叠加城市应用场景需求增长")

    # 政策适配情况
    st.markdown("### 🏛 政策匹配")
    st.success("命中政策：北京智能制造专项补贴、2023年“机器人+”示范名单")
    st.info("政策关键词：专精特新、科技型中小企业、工业母机")

    # 产业链定位与竞品分析
    st.markdown("### 🔗 产业链地位与竞品分析")
    st.markdown("该企业位于人形机器人整机+控制系统层，具备从感知到执行的集成能力。")
    st.markdown("- 上游：伺服电机、仿生材料、芯片模块供应商")
    st.markdown("- 下游：智能制造终端商、政务/教育采购机构")
    st.markdown("- 竞品：优必选、星动纪元、FigureAI")
    st.markdown("- 核心风险：高成本/难量产、缺乏标准接口/平台")
    st.markdown("- 核心机会：政策窗口期+国产替代、场景协同度高")

    # 专利图表
    st.markdown("### 📈 知识产权图谱")
    patent_data = pd.DataFrame({
        "年份": [2021, 2022, 2023]*3,
        "类型": ["发明", "实用新型", "外观设计"]*3,
        "数量": [6, 12, 18, 8, 15, 21, 3, 5, 9]
    })
    chart = alt.Chart(patent_data).mark_bar().encode(
        x="年份:N",
        y="数量:Q",
        color="类型:N",
        column="类型:N"
    )
    st.altair_chart(chart, use_container_width=True)

    # 融资情况
    st.markdown("### 💰 融资情况")
    st.markdown("- 2022年7月：完成C轮融资，金额3亿元，投资方包括红杉中国、高瓴资本")
    st.markdown("- 2021年3月：完成B+轮融资，金额1.2亿元")

    # 招投标
    st.markdown("### 📋 中标记录")
    st.markdown("- 2023年6月：北京市政务机器人项目，中标金额1200万元")
    st.markdown("- 2022年12月：山东教育局智慧教室项目，中标金额600万元")

    # 负面信息
    st.markdown("### ⚠️ 风险与负面信息")
    st.warning("2022年被合作方起诉合同纠纷，已法院调解结案")
    st.warning("2023年6月收到产品质量整改通知")

    # 金融产品建议
    st.markdown("### 🧩 金融产品适配建议")
    st.markdown("推荐产品：科技型企业专项贷、设备融资租赁、订单贷")
    st.success("产品适配度：高 - 可匹配政采订单与科技补贴叠加企业特征")

# ===== ④ 标记操作区 =====
    st.markdown("---")
    st.subheader("📝 客户标记与尽调任务池")
    mark_status = st.radio("是否推荐进入尽调：", ["进入尽调", "暂不适配", "稍后跟进"])
    remark = st.text_area("备注说明：")
    if st.button("✅ 加入尽调任务池"):
        st.success(f"已将【{selected_client}】加入尽调任务池！标记为：{mark_status}")

    # ===== 跳转至尽调助手模块 =====
    if st.button("🧮 一键进入尽调助手"):
        st.session_state.active_client = selected_client
        st.switch_page("03_尽调助手.py")


