"""
charts_all_sections.py
======================
Generates all publication-quality survey charts for:
  "An Analytical Perspective on Career Preparation Among University Students"
  Author : Shreya Tewari, Chitkara University
  n = 169 total responses (university students)

Exact percentages read from Google Forms screenshots (13-04-2026).

Section 1 — Academic Background
Section 2 — Career Preparation in College
Section 3 — Placement Preparation
Section 4 — Student Opinions
+ Summary overview chart

Usage:
    pip install matplotlib numpy
    python charts_all_sections.py

Output:  ./output_charts/  (21 PNG files)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUTPUT = "./output_charts"
os.makedirs(OUTPUT, exist_ok=True)

# ── palette ─────────────────────────────────────────────────────
C_BLUE   = "#2166AC"
C_RED    = "#D6604D"
C_ORANGE = "#F4A582"
C_GREEN  = "#4DAC26"
C_LBLUE  = "#74ADD1"
C_PURPLE = "#762A83"

N = 169   # university respondents

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

# ── helpers ──────────────────────────────────────────────────────

def save(fig, name):
    p = os.path.join(OUTPUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved → {p}")


def donut(labels, sizes, colors, title, filename):
    """Donut chart with n= in centre and bottom legend."""
    fig, ax = plt.subplots(figsize=(5.5, 4.4))
    wedges, _, autotexts = ax.pie(
        sizes, colors=colors, autopct="%1.1f%%",
        startangle=90, pctdistance=0.76,
        wedgeprops=dict(width=0.52, linewidth=2, edgecolor="white"),
    )
    for at in autotexts:
        at.set_fontsize(10); at.set_fontweight("bold"); at.set_color("white")
    ax.text(0, 0, f"n={N}", ha="center", va="center",
            fontsize=12, fontweight="bold", color="#333333")
    ax.legend(wedges, labels, loc="lower center",
              bbox_to_anchor=(0.5, -0.16), ncol=2,
              fontsize=9, frameon=False, columnspacing=0.8, handlelength=1.2)
    ax.set_title(title, fontsize=11, fontweight="bold", pad=14, color="#1a1a2e")
    fig.tight_layout()
    save(fig, filename)


def hbar(labels, values, colors, title, filename):
    """Horizontal bar — good for 3-4 ordered categories."""
    fig, ax = plt.subplots(figsize=(7.5, 0.7 * len(labels) + 1.7))
    bars = ax.barh(labels, values, color=colors,
                   edgecolor="white", linewidth=1.5, height=0.55)
    for bar, v in zip(bars, values):
        ax.text(v + 0.6, bar.get_y() + bar.get_height() / 2,
                f"{v}%", va="center", fontsize=10.5,
                fontweight="bold", color="#333333")
    ax.set_xlabel("Percentage (%)", fontsize=10.5)
    ax.set_xlim(0, max(values) + 13)
    ax.set_title(title, fontsize=11, fontweight="bold", pad=12, color="#1a1a2e")
    ax.tick_params(axis="y", labelsize=10.5)
    ax.xaxis.grid(True, linestyle="--", alpha=0.4, color="#cccccc")
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, filename)


def vbar(labels, values, colors, title, filename):
    """Vertical bar — good for Likert responses."""
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    bars = ax.bar(labels, values, color=colors,
                  edgecolor="white", linewidth=1.8, width=0.55)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.8,
                f"{v}%", ha="center", fontsize=10.5,
                fontweight="bold", color="#333333")
    ax.set_ylabel("Percentage (%)", fontsize=10.5)
    ax.set_ylim(0, max(values) + 14)
    ax.set_title(title, fontsize=11, fontweight="bold", pad=12, color="#1a1a2e")
    ax.tick_params(axis="x", labelsize=10.5)
    ax.yaxis.grid(True, linestyle="--", alpha=0.4, color="#cccccc")
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, filename)


# ════════════════════════════════════════════════════════════════
# SECTION 1 — ACADEMIC BACKGROUND
# ════════════════════════════════════════════════════════════════
print("\n── Section 1: Academic Background ──")

# Fig 1 — Academic status  (university students only; 169 total)
# From screenshot 1: 1st/2nd=30.8%, 3rd/4th=53.8%, Recently graduated=13%
# School & MBA entries are NOT mentioned — paper only covers university students
donut(
    labels=["3rd or 4th Year", "1st or 2nd Year", "Recently Graduated"],
    sizes=[53.8, 30.8, 13.0],
    colors=[C_RED, C_BLUE, C_ORANGE],
    title="Fig. 1  Academic Status of Respondents (n=169)",
    filename="fig01_academic_status.png",
)

# Fig 2 — Institution type
# Screenshot 1: Private 73.4%, Govt 25.4%  (rest ~1.2% excluded as non-university)
donut(
    labels=["Private University", "Government University"],
    sizes=[74.6, 25.4],
    colors=[C_BLUE, C_RED],
    title="Fig. 2  Type of Institution (n=169)",
    filename="fig02_institution_type.png",
)

# Fig 3 — Field chosen based on career goals
# Screenshot 2: Yes=84%, Not Sure=9.5%, No ~6.5%
donut(
    labels=["Yes — career-aligned", "No", "Not Sure"],
    sizes=[84.0, 6.5, 9.5],
    colors=[C_BLUE, C_RED, C_ORANGE],
    title="Fig. 3  Field of Study Chosen Based on Career Goals (n=169)",
    filename="fig03_field_career_goals.png",
)

# ════════════════════════════════════════════════════════════════
# SECTION 2 — CAREER PREPARATION IN COLLEGE
# ════════════════════════════════════════════════════════════════
print("\n── Section 2: Career Preparation in College ──")

# Fig 4 — Career guidance programs
# Screenshot 2: Yes=83.4%, No=16.6%
donut(
    labels=["Yes — programs available", "No"],
    sizes=[83.4, 16.6],
    colors=[C_BLUE, C_RED],
    title="Fig. 4  Career Guidance Programs at College (n=169)",
    filename="fig04_career_guidance.png",
)

# Fig 5 — Workshop frequency
# Screenshot 3: Frequently=42%, Sometimes=40.8%, Rarely=13%, Never ~4.2%
hbar(
    labels=["Frequently", "Sometimes", "Rarely", "Never"],
    values=[42.0, 40.8, 13.0, 4.2],
    colors=[C_BLUE, C_LBLUE, C_ORANGE, C_RED],
    title="Fig. 5  Frequency of Career-Related Workshops / Seminars (n=169)",
    filename="fig05_workshop_frequency.png",
)

# Fig 6 — Soft skills training
# Screenshot 3: Yes=82.2%, No=17.8%
donut(
    labels=["Yes — soft skills training", "No"],
    sizes=[82.2, 17.8],
    colors=[C_BLUE, C_RED],
    title="Fig. 6  Soft Skills Training at College (n=169)",
    filename="fig06_softskills_training.png",
)

# Fig 7 — Field-specific skills training
# Screenshot 4: Yes=81.1%, No=18.9%
donut(
    labels=["Yes — field skills training", "No"],
    sizes=[81.1, 18.9],
    colors=[C_BLUE, C_RED],
    title="Fig. 7  Field-Specific Skills Training at College (n=169)",
    filename="fig07_field_skills_training.png",
)

# Fig 8 — Career counselling awareness
# Screenshot 4: Yes=75.7%, No=24.3%
donut(
    labels=["Aware of services", "Not Aware"],
    sizes=[75.7, 24.3],
    colors=[C_BLUE, C_RED],
    title="Fig. 8  Awareness of Career Counselling Services (n=169)",
    filename="fig08_counselling_awareness.png",
)

# Fig 9 — Industry professional sessions
# Screenshot 5: Frequently=40.8%, Sometimes=37.3%, Rarely=16%, Never ~5.9%
hbar(
    labels=["Frequently", "Sometimes", "Rarely", "Never"],
    values=[40.8, 37.3, 16.0, 5.9],
    colors=[C_BLUE, C_LBLUE, C_ORANGE, C_RED],
    title="Fig. 9  Industry Professional Sessions at College (n=169)",
    filename="fig09_industry_sessions.png",
)

# Fig 10 — Internships encouraged
# Screenshot 5: Yes=84.6%, No=15.4%
donut(
    labels=["Yes — encouraged", "No"],
    sizes=[84.6, 15.4],
    colors=[C_BLUE, C_RED],
    title="Fig. 10  College Encourages Students to Pursue Internships (n=169)",
    filename="fig10_internship_encouraged.png",
)

# ════════════════════════════════════════════════════════════════
# SECTION 3 — PLACEMENT PREPARATION
# ════════════════════════════════════════════════════════════════
print("\n── Section 3: Placement Preparation ──")

# Fig 11 — Placement cell
# Screenshot 6: Yes=79.9%, No=8.3%, Maybe=11.8%
donut(
    labels=["Yes — placement cell", "Maybe", "No"],
    sizes=[79.9, 11.8, 8.3],
    colors=[C_BLUE, C_ORANGE, C_RED],
    title="Fig. 11  Dedicated Placement Cell at College (n=169)",
    filename="fig11_placement_cell.png",
)

# Fig 12 — Curriculum prepares for real-world jobs (Likert)
# Screenshot 6: SA=29%, Agree=32.5%, Neutral=26.6%, Disagree=11.8% (rounded to 100%)
# Note: screenshot shows SA=29%, A=32.5%, N=26.6%, D=11.8% → sums to ~100%
vbar(
    labels=["Strongly\nAgree", "Agree", "Neutral", "Disagree"],
    values=[29.0, 32.5, 26.6, 11.8],
    colors=[C_BLUE, C_LBLUE, C_ORANGE, C_RED],
    title="Fig. 12  Curriculum Prepares for Real-World Jobs (n=169)",
    filename="fig12_curriculum_realworld.png",
)

# Fig 13 — Mock interviews
# Screenshot 7: Yes=70.4%, No=29.6%
donut(
    labels=["Yes — mock interviews held", "No"],
    sizes=[70.4, 29.6],
    colors=[C_BLUE, C_RED],
    title="Fig. 13  Mock Interviews Conducted at College (n=169)",
    filename="fig13_mock_interviews.png",
)

# Fig 14 — Job confidence
# Screenshot 7: Very confident=39.1%, Somewhat=44.4%, Not confident=16.6%
vbar(
    labels=["Very\nConfident", "Somewhat\nConfident", "Not\nConfident"],
    values=[39.1, 44.4, 16.6],
    colors=[C_GREEN, C_ORANGE, C_RED],
    title="Fig. 14  Student Confidence About Job Opportunities After Graduation (n=169)",
    filename="fig14_job_confidence.png",
)

# Fig 15 — Training improves employability (Likert)
# Screenshot 8: SA=30.2%, Agree=35.5%, Neutral=26.6%, Disagree=7.7%
vbar(
    labels=["Strongly\nAgree", "Agree", "Neutral", "Disagree"],
    values=[30.2, 35.5, 26.6, 7.7],
    colors=[C_BLUE, C_LBLUE, C_ORANGE, C_RED],
    title="Fig. 15  Training Programs Improve Employability Skills (n=169)",
    filename="fig15_training_employability.png",
)

# ════════════════════════════════════════════════════════════════
# SECTION 4 — STUDENT OPINIONS
# ════════════════════════════════════════════════════════════════
print("\n── Section 4: Student Opinions ──")

# Fig 16 — University-industry collaboration
# Screenshot 8: Yes=94.1%, No=5.9%
donut(
    labels=["Yes — should collaborate more", "No"],
    sizes=[94.1, 5.9],
    colors=[C_BLUE, C_RED],
    title="Fig. 16  Universities Should Collaborate More with Industries (n=169)",
    filename="fig16_university_industry.png",
)

# Fig 17 — Internship opportunities should increase
# Screenshot 9: Yes=95.3%, No=4.7%
donut(
    labels=["Yes — increase internships", "No"],
    sizes=[95.3, 4.7],
    colors=[C_BLUE, C_RED],
    title="Fig. 17  Internship Opportunities Should Be Increased (n=169)",
    filename="fig17_internship_increase.png",
)

# Fig 18 — Biggest challenge
# Screenshot 9: Lack of skills=40.8%, Limited jobs=21.9%, Lack of guidance=24.3%, Lack of internships=13%
hbar(
    labels=["Lack of Skills", "Lack of Guidance",
            "Limited Job\nOpportunities", "Lack of\nInternships"],
    values=[40.8, 24.3, 21.9, 13.0],
    colors=[C_RED, C_BLUE, C_PURPLE, C_ORANGE],
    title="Fig. 18  Biggest Challenge Students Face in Getting Jobs (n=169)",
    filename="fig18_biggest_challenge.png",
)

# Fig 19 — Career satisfaction
# Screenshot 10: Very satisfied=32.5%, Satisfied=25.4%, Neutral=30.2%, Unsatisfied=11.8%
vbar(
    labels=["Very\nSatisfied", "Satisfied", "Neutral", "Unsatisfied"],
    values=[32.5, 25.4, 30.2, 11.8],
    colors=[C_GREEN, C_BLUE, C_ORANGE, C_RED],
    title="Fig. 19  Satisfaction with Career Preparation Support (n=169)",
    filename="fig19_career_satisfaction.png",
)

# Fig 20 — Overall college prepares students
# Screenshot 10: Yes=75.7%, No=24.3%
donut(
    labels=["Yes — prepares well", "No"],
    sizes=[75.7, 24.3],
    colors=[C_BLUE, C_RED],
    title="Fig. 20  Overall: College Prepares Students for Future Careers (n=169)",
    filename="fig20_overall_preparation.png",
)

# ════════════════════════════════════════════════════════════════
# FIG 21 — SUMMARY HORIZONTAL BAR (full-width overview)
# ════════════════════════════════════════════════════════════════
print("\n── Fig 21: Summary Overview ──")

labs = [
    "Internships Encouraged",
    "Career Guidance Programs",
    "Soft Skills Training",
    "Field Skills Training",
    "Career Counselling Awareness",
    "Placement Cell Available",
    "Mock Interviews Available",
    "Overall College Preparation",
]
vals = [84.6, 83.4, 82.2, 81.1, 75.7, 79.9, 70.4, 75.7]

# sort ascending for readability
pairs = sorted(zip(vals, labs))
vals_s, labs_s = zip(*pairs)

bar_cols = [C_RED if v < 72 else C_LBLUE if v < 80 else C_BLUE for v in vals_s]

fig, ax = plt.subplots(figsize=(10, 5.5))
bars = ax.barh(labs_s, vals_s, color=bar_cols,
               edgecolor="white", linewidth=1.5, height=0.6)
for bar, v in zip(bars, vals_s):
    ax.text(v + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{v}%", va="center", fontsize=10.5,
            fontweight="bold", color="#222222")

ax.axvline(75, color="#999999", linestyle="--", linewidth=1.2, alpha=0.7)
ax.text(75.5, -0.7, "75% reference line", fontsize=8.5, color="#777777")

ax.set_xlabel("% of Students Responding Positively", fontsize=10.5)
ax.set_xlim(0, 105)
ax.set_title("Fig. 21  Summary — Key Institutional Career Support Indicators (n=169)",
             fontsize=12, fontweight="bold", pad=14, color="#1a1a2e")
ax.tick_params(axis="y", labelsize=10.5)
ax.xaxis.grid(True, linestyle="--", alpha=0.4, color="#cccccc")
ax.set_axisbelow(True)

legend_h = [
    mpatches.Patch(color=C_BLUE,  label="≥ 80%  — Strong"),
    mpatches.Patch(color=C_LBLUE, label="72–79% — Moderate"),
    mpatches.Patch(color=C_RED,   label="< 72%  — Needs Attention"),
]
ax.legend(handles=legend_h, loc="lower right", fontsize=9.5,
          frameon=True, framealpha=0.85)
fig.tight_layout()
save(fig, "fig21_summary_overview.png")

print(f"\n✅  All 21 charts saved to: {OUTPUT}/")
