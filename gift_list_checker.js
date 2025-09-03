const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    if (!gifts || gifts.length === 0) return ctx.reply('No gifts available');

    let result = '';
    for (const g of gifts) {
      const emoji = g.sticker?.emoji || '🎁';
      result += `${emoji} ${g.star_count}⭐`;
      if (g.remaining_count !== undefined && g.total_count !== undefined) {
        result += ' 可升级';
      }
      result += '\n';
    }

    ctx.reply(result.trim());
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();
