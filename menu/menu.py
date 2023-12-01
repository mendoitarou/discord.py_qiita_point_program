class select_menu(discord.ui.View):
  @discord.ui.select(
    cls=discord.ui.Select,
    placeholder="未選択時に表示されるテキスト",
    options=[
      # 選択肢をここに記述
      discord.SelectOption(value='選択後動作で受け取る値', label='表示テキスト', description='説明'),
    ],
  )
  async def selectMenu(self, interaction: discord.Interaction, select: discord.ui.Select):
    await interaction.response.send_message(f'"{str(select.values[0])}"が選択されました')

def add_menu():
  select_menu = select_menu()
  select_menu.selectMenu.add_option(
    label='表示テキスト_2',
    value='選択後動作で受け取る値_2',
   description='説明_2'
  )