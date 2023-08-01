from googletrans import Translator
from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from plugins.helpers.database import find , insert
from plugins.helpers.list import list
from Script import script
from info import SP

@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Update Channel", url='https://t.me/hbbotz'
                                        ),
                                    ],
				    [
                                        InlineKeyboardButton(
                                            "𝘊𝘭𝘰𝘴𝘦", callback_data="close_data"
                                        )
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"translated from {fromt.capitalize()} to {to.capitalize()}\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			except:
			   	await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			

		except :
			print("error")
	else:
	                 m = await message.reply_photo(
                         photo=(SP),
                         caption=(START_TXT.format(message.from_user.mention)),
                         reply_markup=InlineKeyboardMarkup(
                                   [[
                                     InlineKeyboardButton('Close', callback_data="close_data"),
                                                                         
                                   ]]
                         ),
                         parse_mode=enums.ParseMode.HTML
) 

                     

#list py   


list = {
"afrikaans":"af",
"albanian":"sq",
"amharic":"am",
"arabic":"ar",
"armenian":"hy",
"azerbaijani":"az",
"basque":"eu",
"belarusian":"be",
"bengali":"bn",
"bosnian":"bs",
"bulgarian":"bg",
"catalan":"ca",
"cebuano":"ceb",
"chinese": "zh",
"corsican":"co",
"croatian":"hr",
"czech":"cs",
"danish":"da",
"dutch":"nl",
"english":"en",
"esperanto":"eo",
"estonian":"et",
"finnish":"fi",
"french":"fr",
"frisian":"fy",
"galician":"gl",
"georgian":"ka",
"german":"de",
"greek":"el",
"gujarati":"gu",
"haitian creole":"ht",
"hausa":"ha",
"hawaiian":"haw",
"hebrew":"he",
"hindi":"hi",
"hmong":"hmn",
"hungarian":"hu",
"icelandic":"is",
"igbo":"ig",
"indonesian":"id",
"irish":"ga",
"italian":"it",
"japanese":"ja",
"javanese":"jv",
"kannada":"kn",
"kazakh":"kk",
"khmer":"km",
"kinyarwanda":"rw",
"korean":"ko",
"kurdish":"ku",
"kyrgyz":"ky",
"lao":"lo",
"latin":"la",
"latvian":"lv",
"lithuanian":"lt",
"luxembourgish":"lb",
"macedonian":"mk",
"malagasy":"mg",
"malay":"ms",
"malayalam":"ml",
"maltese":"mt",
"maori":"mi",
"marathi":"mr",
"mongolian":"mn",
"myanmar":"my",
"nepali":"ne",
"norwegian":"no",
"nyanja":"ny",
"odia":"or",
"pashto":"ps",
"persian":"fa",
"polish":"pl",
"portuguese":"pt",
"punjabi":"pa",
"romanian":"ro",
"russian":"ru",
"samoan":"sm",
"scots gaelic":"gd",
"serbian":"sr",
"sesotho":"st",
"shona":"sn",
"sindhi":"sd",
"sinhala":"si",
"slovak":"sk",
"slovenian":"sl",
"somali":"so",
"spanish":"es",
"sundanese":"su",
"swahili":"sw",
"swedish":"sv",
"tagalog":"tl",
"tajik":"tg",
"tamil":"ta",
"tatar":"tt",
"telugu":"te",
"thai":"th",
"turkish":"tr",
"turkmen":"tk",
"ukrainian":"uk",
"urdu":"ur",
"uyghur":"ug",
"uzbek":"uz",
"vietnamese":"vi",
"welsh":"cy",
"xhosa":"xh",
"yiddish":"yi",
"yoruba":"yo",
"zulu":"zu"}
