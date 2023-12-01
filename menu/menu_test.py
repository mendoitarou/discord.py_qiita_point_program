# ライブラリ読み込み
import discord

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
    await interaction.response.send_message(f'{str(select.values[0])}が選択されました')

# あとから選択肢を追加したい場合
def select_menu_add():
  # メニュー取得
  select_menu = Select_Menu()
  # 項目追加
  select_menu.selectMenu.add_option(
    label='表示テキスト_2',
    value='選択後動作で受け取る値_2',
    description='説明_2'
  )
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