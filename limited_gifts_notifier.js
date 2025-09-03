const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    if (!Array.isArray(gifts) || gifts.length === 0) {
      return ctx.reply('No gifts available');
    }

    const list = gifts.map(g => {
      const emoji = g.sticker?.emoji || '🎁';
      return `${emoji} ${g.star_count}⭐` + (g.remaining_count !== undefined && g.total_count !== undefined ? ' 可升级' : '');
    });

    ctx.reply(list.join('\n'));
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();
