const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.command('gifts', async ctx => {
  try {
    const gifts = await getAvailableGifts();
    if (!gifts?.length) return ctx.reply('No gifts available');
    ctx.reply(gifts.map(g =>
      `${g.sticker?.emoji || '🎁'} ${g.star_count}⭐${(g.remaining_count && g.total_count) ? ' 可升级' : ''}`
    ).join('\n'));
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();
