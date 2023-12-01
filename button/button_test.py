# ライブラリ読み込み
import discord

# ボタン作成
class button_one(discord.ui.Button):
  def __init__(self, *, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str = "ボタン1"):
    super().__init__(style=style, label=label) 
  async def callback(self, interaction: discord.Interaction)
    await interaction.response.send_message('ボタン1が押されました')

class button_two(discord.ui.Button):
  def __init__(self, *, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str = "ボタン2"):
    super().__init__(style=style, label=label) 
  async def callback(self, interaction: discord.Interaction)
    await interaction.response.send_message('ボタン2が押されました！')

@tree.command(name='button_send', sescription='ボタン送信')
async def button_send(interaction: discord.Interaction):
  view = discord.ui.View()
  view.add_item(button_one(style=discord.ButtonStyle.primary))
  view.add_item(button_two(style=discord.ButtonStyle.secondary))
  await interaction.response.send_message(view=view)