import streamlit as st

st.title("🦖 ARK マナガルム 個体値評価＆ブリーディング最適化アプリ")

mode = st.radio("モードを選択してください", ["個体値評価", "ブリーディング最適化"])

# 基準ステータス
reference_stats = {
    "health": 4500,
    "stamina": 1200,
    "melee": 180,
    "weight": 400
}

def evaluate_individual(stats):
    score = {}
    feedback = []
    for stat in ["health", "stamina", "melee", "weight"]:
        user_value = stats.get(stat, 0)
        base = reference_stats[stat]
        ratio = user_value / base
        s = min(int(ratio * 10), 10)
        score[stat] = s

        if s >= 9:
            feedback.append(f"{stat} は非常に優秀です。")
        elif s <= 5:
            feedback.append(f"{stat} はブリーディングの改善候補です。")
        else:
            feedback.append(f"{stat} は平均的です。")

    total = sum(score.values()) / len(score)
    if total >= 8:
        overall = "ブリーディングに非常に適しています。"
    elif total >= 6:
        overall = "まずまずの個体です。"
    else:
        overall = "ブリーディングにはやや不向きです。"

    return score, feedback, overall

def compare_parents(male, female):
    stats = ["health", "stamina", "melee", "weight"]
    ideal_baby = {}
    inherited_from = {}
    for stat in stats:
        if male[stat] > female[stat]:
            ideal_baby[stat] = male[stat]
            inherited_from[stat] = "♂オス"
        else:
            ideal_baby[stat] = female[stat]
            inherited_from[stat] = "♀メス"

    good_stats = sum(1 for s in stats if ideal_baby[s] >= max(male[s], female[s]))
    if good_stats == 4:
        overall = "✅ この組み合わせは非常に優れています！"
    elif good_stats >= 2:
        overall = "👍 良ステが多く、交配価値があります。"
    else:
        overall = "⚠️ 他の組み合わせを検討してもよいかもしれません。"

    return ideal_baby, inherited_from, overall

if mode == "個体値評価":
    st.header("個体ステータス入力")
    hp = st.number_input("体力 (HP)", 0)
    stamina = st.number_input("スタミナ", 0)
    melee = st.number_input("近接攻撃力 (%)", 0)
    weight = st.number_input("重量", 0)

    if st.button("評価する"):
        stats = {
            "health": hp,
            "stamina": stamina,
            "melee": melee,
            "weight": weight
        }
        score, feedback, overall = evaluate_individual(stats)
        st.subheader("評価結果")
        for stat in score:
            st.write(f"{stat}: スコア {score[stat]}")
        st.write("フィードバック:")
        for f in feedback:
            st.write(f"- {f}")
        st.write(f"総合評価: {overall}")

elif mode == "ブリーディング最適化":
    st.header("♂オスのステータス")
    male_hp = st.number_input("オスのHP", 0, key="male_hp")
    male_stamina = st.number_input("オスのスタミナ", 0, key="male_stamina")
    male_melee = st.number_input("オスの近接攻撃力", 0, key="male_melee")
    male_weight = st.number_input("オスの重量", 0, key="male_weight")

    st.header("♀メスのステータス")
    female_hp = st.number_input("メスのHP", 0, key="female_hp")
    female_stamina = st.number_input("メスのスタミナ", 0, key="female_stamina")
    female_melee = st.number_input("メスの近接攻撃力", 0, key="female_melee")
    female_weight = st.number_input("メスの重量", 0, key="female_weight")

    if st.button("ブリーディング評価"):
        male = {
            "health": male_hp,
            "stamina": male_stamina,
            "melee": male_melee,
            "weight": male_weight
        }
        female = {
            "health": female_hp,
            "stamina": female_stamina,
            "melee": female_melee,
            "weight": female_weight
        }
        ideal_baby, inherited_from, overall = compare_parents(male, female)
        st.subheader("理想の子供ステータス")
        for stat in ideal_baby:
            st.write(f"{stat}: {ideal_baby[stat]} （継承元: {inherited_from[stat]}）")
        st.write(f"総合評価: {overall}")
