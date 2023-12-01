# ライブラリ読み込み
import discord
from discord import app_commands
import os
import time

DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    print(f'起動しました！ BOT_Name:{client.user}')
    await tree.sync()

# メニュー関連
class Select_Menu(discord.ui.View):
    @discord.ui.select(
        cls=discord.ui.Select,
        placeholder="未選択時に表示されるテキスト",
        options=[
        #選択肢をここに記述
        discord.SelectOption(value='選択後動作で受け取る値', label='表示テキスト', description='説明'),
        ],
    )
    async def selectMenu(self, interaction: discord.Interaction, select: discord.ui.Select):
        # 選択後の動作
        await interaction.response.send_message(f'"{str(select.values[0])}"が選択されました')

# あとから選択肢を追加したい場合
def select_menu_add():
    # メニュー取得
    select_menu = Select_Menu()
    # 項目追加
    select_menu.selectMenu.add_option(label='表示テキスト_2', value='選択後動作で受け取る値_2', description='説明_2')
    return select_menu

# メニュー送信
@tree.command(name='menu',description='メニューを送信します。')
async def menu_send(interaction: discord.Interaction):
  # メニュー取得
  select_menu = Select_Menu()
  await interaction.response.send_message(view=select_menu)

# 項目追加後送信
@tree.command(name='menu_add',description='メニューにあとから項目を追加して送信します。')
async def menu_add_send(interaction: discord.Interaction):
  # メニュー取得
  select_menu = select_menu_add()
  await interaction.response.send_message(view=select_menu)

# ボタン関連
class button_one(discord.ui.Button):
  def __init__(self, *, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str = "ボタン1"):
    super().__init__(style=style, label=label) 
  async def callback(self, interaction: discord.Interaction):
    await interaction.response.send_message('ボタン1が押されました')

class button_two(discord.ui.Button):
  def __init__(self, *, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str = "ボタン2"):
    super().__init__(style=style, label=label) 
  async def callback(self, interaction: discord.Interaction):
    await interaction.response.send_message('ボタン2が押されました！')

@tree.command(name='button_send', description='ボタン送信')
async def button_send(interaction: discord.Interaction):
  view = discord.ui.View()
  view.add_item(button_one(style=discord.ButtonStyle.primary))
  view.add_item(button_two(style=discord.ButtonStyle.secondary))
  await interaction.response.send_message(view=view)

#遅延テスト
@tree.command(name='defer', description='遅延テスト(処理なし)')
async def defer(interaction: discord.Interaction):
    time.sleep(6)
    await interaction.followup.send(content='処理完了！')

# 遅延対策
@tree.command(name='defer_test', description='遅延テスト')
async def defer_test(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    time.sleep(6)
    #await interaction.delete_original_response()
    await interaction.followup.send(content='処理完了！')

# BOT停止コマンド
@tree.command(name="bot_stop",description="Botを停止します。")
@app_commands.default_permissions(administrator=True)
async def bot_stop(interaction:discord.Interaction):
    await interaction.response.send_message("Botを停止します。", ephemeral=True)
    await client.close()

client.run(DISCORD_TOKEN)