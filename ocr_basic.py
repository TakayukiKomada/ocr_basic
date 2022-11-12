from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]

print(tool)
print(tool.get_name())

img = Image.open("sparta_camp_jp.png")
# img.show()
txt = tool.image_to_string(img, lang="jpn+eng", builder=pyocr.builders.TextBuilder())
print(txt)
# import sys
# from PIL import Image
# import pyocr
# import pyocr.builders

# tools = pyocr.get_available_tools()
# if len(tools) == 0:
#     print("No OCR tool found")
#     sys.exit(1)
# # 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいる
# tool = tools[0]
# print("Will use tool '%s'" % (tool.get_name()))
# # 例: Will use tool 'Tesseract (sh)'
