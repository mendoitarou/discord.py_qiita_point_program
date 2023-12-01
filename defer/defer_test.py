# ライブラリ読み込み
import discord
import time# sleep関数のため

@tree.command(name='defer_test', description='遅延テスト')
async def defer_test(interaction: discord.Interaction):
  await interaction.response.defer(ephemeral=True)
  time.sleep(6)
  await interaction.followup.send(content='処理完了！')