import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm

# Verify font file exists
font_path = "Padauk-Regular.ttf"
if not os.path.exists(font_path):
    raise FileNotFoundError(
        f"Font file {font_path} not found. Please download Padauk-Regular.ttf and place it in the same directory as this script.")

# Initialize PDF
pdf = canvas.Canvas("employment_contract.pdf", pagesize=A4)
width, height = A4

# Register Padauk font
pdfmetrics.registerFont(TTFont("Padauk", font_path))

# Set initial font and position
pdf.setFont("Padauk", 14)
y_position = height - 20 * mm

# Header
pdf.drawCentredString(width / 2, y_position, "အလုပ်သမားစာချုပ်")
y_position -= 10 * mm

# Contract details
pdf.setFont("Padauk", 12)
contract_details = [
    ("စာချုပ်နံပါတ်:", "[စာချုပ်နံပါတ်ထည့်ရန်]"),
    ("ရက်စွဲ:", "2025-05-21"),
    ("အလုပ်ရှင်:", "[သင့်အမည်/လုပ်ငန်းအမည်]"),
    ("လိပ်စာ:", "[သင့်လုပ်ငန်းလိပ်စာ]"),
    ("ဝန်ထမ်း:", "[ဝန်ထမ်းအမည်ထည့်ရန်]"),
    ("လိပ်စာ:", "[ဝန်ထမ်းလိပ်စာထည့်ရန်]"),
]

for label, value in contract_details:
    pdf.drawString(20 * mm, y_position, f"{label} {value}")
    y_position -= 7 * mm

y_position -= 7 * mm

# Introduction
pdf.drawString(20 * mm, y_position,
               "ဤစာချုပ်သည် အလုပ်ရှင်နှင့် ဝန်ထမ်းအကြား သဘောတူညီမှုတစ်ခုဖြစ်ပြီး အောက်ပါအချက်များကို သဘောတူညီပါသည်။")
y_position -= 10 * mm

# Section 1: Employment Duration
pdf.setFont("Padauk", 12)
pdf.drawString(20 * mm, y_position, "၁. လုပ်ငန်းသက်တမ်း")
y_position -= 7 * mm
pdf.setFont("Padauk", 10)
pdf.drawString(20 * mm, y_position,
               "ဤစာချုပ်သည် [စာချုပ်စတင်ရက်စွဲ] မှစတင်၍ အနည်းဆုံး ၆ လအထိ အကျုံးဝင်ပါသည်။")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "စာချုပ်သက်တမ်းကို နှစ်ဦးနှစ်ဘက်သဘောတူညီမှုဖြင့် သက်တမ်းတိုးနိုင်ပါသည်။")
y_position -= 10 * mm

# Section 2: Salary and Work Hours
pdf.setFont("Padauk", 12)
pdf.drawString(20 * mm, y_position, "၂. လစာနှင့် အလုပ်ချိန်")
y_position -= 7 * mm
pdf.setFont("Padauk", 10)
pdf.drawString(20 * mm, y_position, "• လစာနှုန်းထား:")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position,
               "- ၆ လပိုင်းနှင့် ၇ လပိုင်းတွင် ဝန်ထမ်းတစ်ဦးလျှင် တစ်လလျှင် ၂၀၀,၀၀၀ ကျပ် ပေးချေမည်။")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position,
               "- ၈ လပိုင်း (လိမ္မော်သီးရာသီချိန်) တွင် ဝန်ထမ်းတစ်ဦးလျှင် တစ်လလျှင် ၃၀၀,၀၀၀ ကျပ် ပေးချေမည်။")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position,
               "- အလုပ်မရှိသည့်ရက်များတွင်လည်း လစာကို ပုံမှန်ပေးချေမည်။")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "• အလုပ်ချိန်: အလုပ်ပေါ်မူတည်၍ လုပ်ကိုင်ရမည်ဖြစ်ပြီး၊")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position,
               "အလုပ်ရှင်မှ သတ်မှတ်ထားသော လုပ်ငန်းတာဝန်များကို ထမ်းဆောင်ရမည်။")
y_position -= 10 * mm

# Section 3: Benefits
pdf.setFont("Padauk", 12)
pdf.drawString(20 * mm, y_position, "၃. အကျိုးခံစားခွင့်များ")
y_position -= 7 * mm
pdf.setFont("Padauk", 10)
pdf.drawString(20 * mm, y_position,
               "• ကားမောင်းသင်တန်း: ဝန်ထမ်းများအား အလုပ်မရှိသည့်အခါများတွင်")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position, "ကားမောင်းနည်းသင်တန်းကို အခမဲ့ပေးမည်။")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "• အင်တာနက်အသုံးပြုခွင့်: ဝန်ထမ်းများအား လုပ်ငန်းခွင်အတွင်း")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position, "အင်တာနက်အခမဲ့အသုံးပြုခွင့်ပေးမည်။")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "• အစားအသောက်: ဝန်ထမ်းများအား အလုပ်ရှင်မှ ထောက်ပံ့ပေးသော")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position, "အစားအသောက်များကို အခမဲ့ရရှိမည်။")
y_position -= 10 * mm

# Section 4: Termination
pdf.setFont("Padauk", 12)
pdf.drawString(20 * mm, y_position, "၄. စာချုပ်ရပ်ဆိုင်းမှု")
y_position -= 7 * mm
pdf.setFont("Padauk", 10)
pdf.drawString(20 * mm, y_position,
               "• ဝန်ထမ်းသည် အနည်းဆုံး ၆ လအထိ လုပ်ကိုင်ရန် ကတိပြုပါသည်�।")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "• စာချုပ်သက်တမ်းမပြည့်မီ ဖျက်သိမ်းလိုပါက နှစ်ဦးနှစ်ဘက်သဘောတူညီမှုဖြင့်")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position,
               "ရက် ၃၀ ကြိုတင်အကြောင်းကြားပြီး ရပ်ဆိုင်းနိုင်သည်။")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "• အလုပ်ရှင်မှ စာချုပ်ဖျက်သိမ်းလိုပါက ဝန်ထမ်းအား")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position, "ရက် ၃၀ ကြိုတင်အကြောင်းကြားရမည်။")
y_position -= 10 * mm

# Section 5: Other Agreements
pdf.setFont("Padauk", 12)
pdf.drawString(20 * mm, y_position, "၅. အခြားသဘောတူညီချက်များ")
y_position -= 7 * mm
pdf.setFont("Padauk", 10)
pdf.drawString(20 * mm, y_position,
               "• ဝန်ထမ်းသည် အလုပ်ရှင်မှ သတ်မှတ်ထားသော လုပ်ငန်းဆိုင်ရာ")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position, "စည်းမျဉ်းစည်းကမ်းများကို လိုက်နာရမည်။")
y_position -= 5 * mm
pdf.drawString(20 * mm, y_position,
               "• ဤစာချုပ်တွင် ဖော်ပြမထားသော အခြားအချက်များကို")
y_position -= 5 * mm
pdf.drawString(25 * mm, y_position,
               "နှစ်ဦးနှစ်ဘက်သဘောတူညီမှုဖြင့် ထပ်မံဖြည့်စွမ်းနိုင်သည်။")
y_position -= 10 * mm

# Signature Section
pdf.setFont("Padauk", 10)
pdf.drawString(20 * mm, y_position,
               "ဤစာချုပ်ကို နှစ်ဦးနှစ်ဘက် သဘောတူညီမှုဖြင့် လက်မှတ်ရေးထိုးပါသည်။")
y_position -= 10 * mm
pdf.drawString(20 * mm, y_position, "အလုပ်ရှင်: _________________________")
pdf.drawString(100 * mm, y_position, "ဝန်ထမ်း: _________________________")
y_position -= 7 * mm
pdf.drawString(20 * mm, y_position, "အမည်: [သင့်အမည်]")
pdf.drawString(100 * mm, y_position, "အမည်: [ဝန်ထမ်းအမည်]")
y_position -= 7 * mm
pdf.drawString(20 * mm, y_position, "ရက်စွဲ: [ရက်စွဲထည့်ရန်]")
pdf.drawString(100 * mm, y_position, "ရက်စွဲ: [ရက်စွဲထည့်ရန်]")

# Footer (Page Number)
pdf.setFont("Padauk", 8)
pdf.drawString(20 * mm, 10 * mm, f"စာမျက်နှာ {pdf.getPageNumber()}")

# Save PDF
pdf.showPage()
pdf.save()
